

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_payment_usercourse'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
