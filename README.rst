=====
T_email
=====

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
