import subprocess

# تحديد الأمر الذي تريد تشغيله
command = ['tmate', '-v']  # يمكنك تعديل هذا الأمر حسب الحاجة

# فتح ملف للكتابة
with open('output.txt', 'w') as file:
    # تشغيل الأمر وحفظ النتائج في الملف
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    # كتابة النتائج في الملف
    file.write('STDOUT:\n')
    file.write(stdout.decode())
    file.write('\nSTDERR:\n')
    file.write(stderr.decode())
