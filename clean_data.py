import pandas as pd
import numpy as np

print("🚀 جاري بدء عملية تنظيف البيانات...")

# 1. قراءة الملف (مع تخطي السطور الأولى غير المهمة)
# لاحظنا أن العناوين الحقيقية تبدأ في السطر رقم 5 تقريباً
# التعديل: إضافة encoding='latin1'
df = pd.read_csv('raw_data.csv', header=4, encoding='latin1')
# 2. تنظيف أسماء الأعمدة
# العمود الأول اسمه طويل جداً، سنسميه "Program" والعمود الأخير سنحذفه لأنه إجمالي
df.rename(columns={df.columns[0]: 'Program_Stream'}, inplace=True)
# حذف عمود الإجمالي الأخير لأنه يسبب تكراراً في Power BI (البرنامج يحسبه تلقائياً)
df = df.iloc[:, :-1] 

# 3. معالجة عمود نوع الدعم (Type of Support)
# المشكلة: نوع الدعم مكتوب مرة واحدة وتحته فراغ. 
# الحل: ننشئ عموداً جديداً ونملأ الفراغات بالقيمة السابقة (Forward Fill)
df['Type_of_Support'] = df['Program_Stream'].apply(lambda x: x if x in [
    'GRANT', 'NON REPAYABLE CONTRIBUTION', 'CONDITIONAL REPAYABLE CONTRIBUTION', 
    'REPAYABLE CONTRIBUTION', 'GOVERNMENT PERFORMED SERVICES', 'OTHER'
] else np.nan)
df['Type_of_Support'] = df['Type_of_Support'].ffill()

# 4. تنظيف عمود البرامج
# نحذف الصفوف التي هي عبارة عن عناوين رئيسية أو مجاميع فرعية
df = df[df['Program_Stream'] != df['Type_of_Support']] # حذف صف العنوان
df = df[~df['Program_Stream'].str.contains('Subtotal', na=False, case=False)] # حذف المجاميع
df = df[~df['Program_Stream'].str.contains('Total value', na=False, case=False)] # حذف الإجمالي النهائي
df = df[~df['Program_Stream'].str.contains('Source:', na=False)] # حذف الملاحظات في الأسفل

# 5. تحويل البيانات من Wide إلى Long (Unpivot) - أهم خطوة!
# سنجعل السنوات كلها في عمود واحد اسمه "Year" والقيم في عمود "Amount"
df_melted = df.melt(id_vars=['Type_of_Support', 'Program_Stream'], 
                    var_name='Year', 
                    value_name='Amount')

# 6. تنظيف الأرقام (Amount)
def clean_currency(x):
    if isinstance(x, str):
        # حذف الفواصل
        x = x.replace(',', '')
        # استبدال الرموز X و ... بصفر أو قيمة فارغة
        if x == 'X' or x == '...' or x == '..':
            return 0
    return x

df_melted['Amount'] = df_melted['Amount'].apply(clean_currency)
# تحويل العمود لأرقام
df_melted['Amount'] = pd.to_numeric(df_melted['Amount'])

# 7. حفظ الملف النظيف
output_file = 'clean_canadian_grants.csv'
df_melted.to_csv(output_file, index=False)

print("-" * 30)
print(f"✅ تم التنظيف بنجاح!")
print(f"📄 الملف الجديد: {output_file}")
print(df_melted.head())