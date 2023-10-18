from frontend import BankApp


def main():
    app = BankApp("mybank.db")
    app.run()


if __name__ == '__main__':
    main()


# برای ساخت فایل exe کدهای زیر را در خط فرمان ترمینال دایرکتوری پروژه اجرا کنید
# pip install  Pyinstaller
# or
# pip install https://github.com/pyinstaller/pyinstaller/archive/develop.zip
# pyinstaller --onefile main.py
