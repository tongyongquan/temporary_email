=====
T_email
=====
临时邮箱接口返回邮箱地址和邮件内容,用做接收验证码

Quick start
-----------
pip instll temporaty_email

.. code:: python

    from temporaty_email.temporary_email import TemporaryEmail
    t_email = TemporaryEmail()
    print(t_email.get_email_address())
    while True:
        if t_email.check_received_email():
            content = t_email.get_email_content()
            print(content)
            break
