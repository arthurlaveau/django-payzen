# Generated by Django 4.1 on 2024-03-19 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomPaymentConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MultiPaymentConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.PositiveIntegerField()),
                ('count', models.PositiveIntegerField()),
                ('period', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ThemeConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('success_footer_msg_return', models.TextField(blank=True, null=True)),
                ('cancel_footer_msg_return', models.TextField(blank=True, null=True)),
                ('secure_message', models.TextField(blank=True, null=True)),
                ('secure_message_register', models.TextField(blank=True, null=True)),
                ('site_id_label', models.TextField(blank=True, null=True)),
                ('css_for_payment', models.URLField(blank=True, null=True)),
                ('css_for_payment_mobile', models.URLField(blank=True, null=True)),
                ('header_for_mail', models.URLField(blank=True, null=True)),
                ('footer_for_mail', models.URLField(blank=True, null=True)),
                ('shop_logo', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VADContract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cb_contract_num', models.CharField(max_length=32)),
                ('amex_contract_num', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vads_cust_address', models.CharField(blank=True, max_length=255, null=True)),
                ('vads_cust_address_number', models.CharField(blank=True, max_length=5, null=True)),
                ('vads_cust_country', models.CharField(blank=True, max_length=2, null=True)),
                ('vads_cust_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('vads_cust_id', models.CharField(blank=True, max_length=63, null=True)),
                ('vads_cust_name', models.CharField(blank=True, max_length=127, null=True)),
                ('vads_cust_last_name', models.CharField(blank=True, max_length=63, null=True)),
                ('vads_cust_first_name', models.CharField(blank=True, max_length=63, null=True)),
                ('vads_cust_cell_phone', models.CharField(blank=True, max_length=32, null=True)),
                ('vads_cust_phone', models.CharField(blank=True, max_length=32, null=True)),
                ('vads_cust_title', models.CharField(blank=True, max_length=63, null=True)),
                ('vads_cust_city', models.CharField(blank=True, max_length=63, null=True)),
                ('vads_cust_status', models.CharField(blank=True, max_length=63, null=True)),
                ('vads_cust_state', models.CharField(blank=True, max_length=63, null=True)),
                ('vads_cust_zip', models.CharField(blank=True, max_length=63, null=True)),
                ('vads_language', models.CharField(blank=True, max_length=2, null=True)),
                ('vads_order_id', models.CharField(blank=True, max_length=32, null=True)),
                ('vads_order_info', models.CharField(blank=True, max_length=255, null=True)),
                ('vads_order_info2', models.CharField(blank=True, max_length=255, null=True)),
                ('vads_order_info3', models.CharField(blank=True, max_length=255, null=True)),
                ('vads_ship_to_name', models.CharField(blank=True, max_length=127, null=True)),
                ('vads_ship_to_first_name', models.CharField(blank=True, max_length=63, null=True)),
                ('vads_ship_to_last_name', models.CharField(blank=True, max_length=63, null=True)),
                ('vads_ship_to_street_number', models.CharField(blank=True, max_length=5, null=True)),
                ('vads_ship_to_street', models.CharField(blank=True, max_length=255, null=True)),
                ('vads_ship_to_street2', models.CharField(blank=True, max_length=255, null=True)),
                ('vads_ship_to_zip', models.CharField(blank=True, max_length=63, null=True)),
                ('vads_ship_to_city', models.CharField(blank=True, max_length=63, null=True)),
                ('vads_ship_to_country', models.CharField(blank=True, max_length=2, null=True)),
                ('vads_ship_to_phone_num', models.CharField(blank=True, max_length=32, null=True)),
                ('vads_ship_to_state', models.CharField(blank=True, max_length=255, null=True)),
                ('vads_threeds_enrolled', models.CharField(blank=True, choices=[('Y', 'Y'), ('N', 'N'), ('U', 'U')], max_length=1, null=True)),
                ('vads_threeds_cavv', models.CharField(blank=True, max_length=28, null=True)),
                ('vads_threeds_eci', models.CharField(blank=True, max_length=2, null=True)),
                ('vads_threeds_xid', models.CharField(blank=True, max_length=28, null=True)),
                ('vads_threeds_cavvAlgorithm', models.CharField(blank=True, choices=[('0', 'HMAC'), ('1', 'CVV'), ('2', 'CVV_ATN'), ('3', 'Mastercard SPA')], max_length=1, null=True)),
                ('vads_threeds_status', models.CharField(blank=True, choices=[('Y', 'U'), ('N', 'N'), ('U', 'U'), ('A', 'A')], max_length=1, null=True)),
                ('vads_threeds_sign_valid', models.BooleanField(null=True)),
                ('vads_threeds_error_code', models.CharField(blank=True, max_length=2, null=True)),
                ('vads_threeds_exit_status', models.CharField(blank=True, max_length=2, null=True)),
                ('vads_warranty_result', models.CharField(blank=True, max_length=13, null=True)),
                ('vads_available_languages', models.TextField(blank=True, null=True)),
                ('vads_theme_config', models.CharField(blank=True, max_length=255, null=True)),
                ('vads_shop_url', models.URLField(blank=True, null=True)),
                ('vads_shop_name', models.CharField(blank=True, max_length=255, null=True)),
                ('signature', models.CharField(max_length=40)),
                ('vads_ctx_mode', models.CharField(choices=[('TEST', 'TEST'), ('PRODUCTION', 'PRODUCTION')], max_length=10)),
                ('vads_url_check_src', models.CharField(blank=True, choices=[('PAY', 'PAY'), ('BO', 'BO'), ('BATCH', 'BATCH'), ('BATCH_AUTO', 'BATCH_AUTO'), ('FILE', 'FILE'), ('REC', 'REC'), ('MERCH_BO', 'MERCH_BO')], max_length=10, null=True)),
                ('vads_version', models.CharField(max_length=2)),
                ('vads_trans_date', models.CharField(max_length=14)),
                ('vads_action_mode', models.CharField(blank=True, choices=[('INTERACTIVE', 'INTERACTIVE'), ('SILENT', 'SILENT')], max_length=11, null=True)),
                ('vads_trans_id', models.CharField(max_length=6)),
                ('vads_payment_config', models.TextField(blank=True, null=True)),
                ('vads_sequence_number', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('vads_site_id', models.PositiveIntegerField()),
                ('vads_amount', models.PositiveIntegerField(blank=True, null=True)),
                ('vads_currency', models.CharField(blank=True, choices=[('036', 'Australian dollar'), ('124', 'Canadian dollar'), ('156', 'Chinese Yuan'), ('208', 'Danish Krone'), ('392', 'Japanese Yen'), ('578', 'Norwegian Krone'), ('752', 'Swedish Krona'), ('756', 'Swiss franc'), ('826', 'Pound sterling'), ('840', 'American dollar'), ('953', 'Franc Pacifique (CFP)'), ('978', 'Euro')], max_length=3, null=True)),
                ('vads_effective_amount', models.PositiveIntegerField(blank=True, null=True)),
                ('vads_operation_type', models.CharField(blank=True, choices=[('DEBIT', 'DEBIT'), ('CREDIT', 'CREDIT')], max_length=6, null=True)),
                ('vads_result', models.CharField(choices=[('00', 'Payment successful'), ('02', 'Merchant should contact his bank'), ('05', 'Payment refused'), ('17', 'Payment cancelled by client'), ('30', 'Wrong request format'), ('96', 'Technical error during payment process')], max_length=2)),
                ('vads_validation_mode', models.CharField(blank=True, choices=[('', 'Default shop configuration (using payzen admin)'), ('0', 'Automatic validation'), ('1', 'Manual validation')], max_length=1, null=True)),
                ('vads_trans_status', models.CharField(choices=[('ABANDONED', 'ABANDONED'), ('AUTHORISED', 'AUTHORISED'), ('REFUSED', 'REFUSED'), ('AUTHORISED_TO_VALIDATE', 'AUTHORISED_TO_VALIDATE'), ('WAITING_AUTHORISATION', 'WAITING_AUTHORISATION'), ('EXPIRED', 'EXPIRED'), ('CANCELLED', 'CANCELLED'), ('WAITING_AUTHORISATION_TO_VALIDATE', 'WAITING_AUTHORISATION_TO_VALIDATE'), ('CAPTURED', 'CAPTURED')], max_length=33)),
                ('vads_effective_creation_date', models.CharField(blank=True, max_length=14, null=True)),
                ('vads_presentation_date', models.CharField(blank=True, max_length=14, null=True)),
                ('vads_capture_delay', models.PositiveIntegerField(blank=True, null=True)),
                ('vads_card_brand', models.CharField(blank=True, max_length=50, null=True)),
                ('vads_card_number', models.CharField(blank=True, max_length=16, null=True)),
                ('vads_expiry_month', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('vads_expiry_year', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('vads_contract_used', models.CharField(blank=True, max_length=250, null=True)),
                ('vads_auth_number', models.CharField(blank=True, max_length=6, null=True)),
                ('vads_auth_result', models.CharField(blank=True, max_length=2, null=True)),
                ('vads_auth_mode', models.CharField(blank=True, choices=[('FULL', 'FULL'), ('MARK', 'MARK')], max_length=4, null=True)),
                ('vads_payment_certificate', models.CharField(blank=True, max_length=40, null=True)),
                ('vads_payment_src', models.CharField(blank=True, choices=[('EC', 'EC'), ('MOTO', 'MOTO'), ('CC', 'CC'), ('OTHER', 'OTHER')], max_length=5, null=True)),
                ('vads_contrib', models.CharField(blank=True, max_length=255, null=True)),
                ('vads_user_info', models.CharField(blank=True, max_length=255, null=True)),
                ('vads_ext_trans_id', models.CharField(blank=True, max_length=6, null=True)),
                ('vads_payment_option_code', models.TextField(blank=True, null=True)),
                ('vads_change_rate', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Response',
                'unique_together': {('vads_trans_id', 'vads_site_id', 'vads_trans_date')},
            },
        ),
        migrations.CreateModel(
            name='PaymentRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vads_cust_address', models.CharField(blank=True, max_length=255, null=True)),
                ('vads_cust_address_number', models.CharField(blank=True, max_length=5, null=True)),
                ('vads_cust_country', models.CharField(blank=True, max_length=2, null=True)),
                ('vads_cust_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('vads_cust_id', models.CharField(blank=True, max_length=63, null=True)),
                ('vads_cust_name', models.CharField(blank=True, max_length=127, null=True)),
                ('vads_cust_last_name', models.CharField(blank=True, max_length=63, null=True)),
                ('vads_cust_first_name', models.CharField(blank=True, max_length=63, null=True)),
                ('vads_cust_cell_phone', models.CharField(blank=True, max_length=32, null=True)),
                ('vads_cust_phone', models.CharField(blank=True, max_length=32, null=True)),
                ('vads_cust_title', models.CharField(blank=True, max_length=63, null=True)),
                ('vads_cust_city', models.CharField(blank=True, max_length=63, null=True)),
                ('vads_cust_status', models.CharField(blank=True, max_length=63, null=True)),
                ('vads_cust_state', models.CharField(blank=True, max_length=63, null=True)),
                ('vads_cust_zip', models.CharField(blank=True, max_length=63, null=True)),
                ('vads_language', models.CharField(blank=True, max_length=2, null=True)),
                ('vads_order_id', models.CharField(blank=True, max_length=32, null=True)),
                ('vads_order_info', models.CharField(blank=True, max_length=255, null=True)),
                ('vads_order_info2', models.CharField(blank=True, max_length=255, null=True)),
                ('vads_order_info3', models.CharField(blank=True, max_length=255, null=True)),
                ('vads_ship_to_name', models.CharField(blank=True, max_length=127, null=True)),
                ('vads_ship_to_first_name', models.CharField(blank=True, max_length=63, null=True)),
                ('vads_ship_to_last_name', models.CharField(blank=True, max_length=63, null=True)),
                ('vads_ship_to_street_number', models.CharField(blank=True, max_length=5, null=True)),
                ('vads_ship_to_street', models.CharField(blank=True, max_length=255, null=True)),
                ('vads_ship_to_street2', models.CharField(blank=True, max_length=255, null=True)),
                ('vads_ship_to_zip', models.CharField(blank=True, max_length=63, null=True)),
                ('vads_ship_to_city', models.CharField(blank=True, max_length=63, null=True)),
                ('vads_ship_to_country', models.CharField(blank=True, max_length=2, null=True)),
                ('vads_ship_to_phone_num', models.CharField(blank=True, max_length=32, null=True)),
                ('vads_ship_to_state', models.CharField(blank=True, max_length=255, null=True)),
                ('vads_action_mode', models.CharField(choices=[('INTERACTIVE', 'INTERACTIVE'), ('SILENT', 'SILENT')], default=None, max_length=11)),
                ('vads_amount', models.PositiveIntegerField()),
                ('vads_currency', models.CharField(choices=[('036', 'Australian dollar'), ('124', 'Canadian dollar'), ('156', 'Chinese Yuan'), ('208', 'Danish Krone'), ('392', 'Japanese Yen'), ('578', 'Norwegian Krone'), ('752', 'Swedish Krona'), ('756', 'Swiss franc'), ('826', 'Pound sterling'), ('840', 'American dollar'), ('953', 'Franc Pacifique (CFP)'), ('978', 'Euro')], default=None, max_length=3)),
                ('vads_ctx_mode', models.CharField(choices=[('TEST', 'TEST'), ('PRODUCTION', 'PRODUCTION')], default='XX', max_length=10)),
                ('vads_page_action', models.CharField(default='PAYMENT', max_length=7)),
                ('vads_payment_config', models.TextField()),
                ('vads_site_id', models.PositiveIntegerField(default='XX')),
                ('vads_trans_date', models.CharField(max_length=14)),
                ('vads_trans_id', models.CharField(max_length=6)),
                ('vads_version', models.CharField(default='V2', max_length=2)),
                ('signature', models.CharField(max_length=40)),
                ('vads_capture_delay', models.PositiveIntegerField(blank=True, null=True)),
                ('vads_contrib', models.CharField(blank=True, default='django-payzen v1.0', max_length=255, null=True)),
                ('vads_payment_cards', models.CharField(blank=True, max_length=127, null=True)),
                ('vads_return_mode', models.CharField(blank=True, choices=[('AMEX', 'American Express'), ('AURORE-MULTI', 'AURORE (multi brand)'), ('BUYSTER', 'BUYSTER'), ('CB', 'CB'), ('COFINOGA', 'COFINOGA'), ('E-CARTEBLEUE', 'e blue card'), ('MASTERCARD', 'Eurocard / MasterCard'), ('JCB', 'JCB'), ('MAESTRO', 'Maestro'), ('ONEY', 'ONEY'), ('ONEY_SANDBOX', 'ONEY SANDBOX mode'), ('PAYPAL', 'PAYPAL'), ('PAYPAL_SB', 'PAYPAL SANDBOX mode'), ('PAYSAFECARD', 'PAYSAFECARD'), ('VISA', 'Visa'), ('VISA_ELECTRON', 'Visa Electron'), ('COF3XCB', '3x CB Cofinoga'), ('COF3XCB_SB', '3x CB Cofinoga SANDBOX')], max_length=13, null=True)),
                ('vads_theme_config', models.CharField(blank=True, max_length=255, null=True)),
                ('vads_validation_mode', models.CharField(blank=True, choices=[('', 'Default shop configuration (using payzen admin)'), ('0', 'Automatic validation'), ('1', 'Manual validation')], max_length=1, null=True)),
                ('vads_url_success', models.URLField(blank=True, null=True)),
                ('vads_url_referral', models.URLField(blank=True, null=True)),
                ('vads_url_refused', models.URLField(blank=True, null=True)),
                ('vads_url_cancel', models.URLField(blank=True, null=True)),
                ('vads_url_error', models.URLField(blank=True, null=True)),
                ('vads_url_return', models.URLField(blank=True, null=True)),
                ('vads_user_info', models.CharField(blank=True, max_length=255, null=True)),
                ('vads_shop_name', models.CharField(blank=True, max_length=255, null=True)),
                ('vads_redirect_success_timeout', models.PositiveIntegerField(blank=True, null=True)),
                ('vads_redirect_success_message', models.CharField(blank=True, max_length=255, null=True)),
                ('vads_redirect_error_timeout', models.PositiveIntegerField(blank=True, null=True)),
                ('vads_redirect_error_message', models.CharField(blank=True, max_length=255, null=True)),
                ('custom_payment_config', models.ManyToManyField(to='django_payzen.custompaymentconfig')),
                ('payment_config', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='django_payzen.multipaymentconfig')),
                ('theme', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='django_payzen.themeconfig')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Request',
                'unique_together': {('vads_trans_id', 'vads_site_id', 'vads_trans_date')},
            },
        ),
    ]
