# Generated by Django 4.1.7 on 2024-03-08 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone_number', models.CharField(max_length=20, null=True, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('role', models.CharField(choices=[('responsable-center', 'Responsable-Center'), ('patient', 'Patient'), ('professionnel', 'Professionnel'), ('gerent-stock', 'Gerent-Stock')], default='patient', max_length=20)),
                ('nni', models.CharField(default='', max_length=20)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CentreDeVaccination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('dateNaissance', models.DateField()),
                ('nni', models.BigIntegerField(unique=True)),
                ('sexe', models.CharField(choices=[('homme', 'Homme'), ('femme', 'Femme')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TypeVaccination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField(default='')),
                ('sexe_cible', models.CharField(choices=[('homme', 'Homme'), ('femme', 'Femme'), ('tous', 'tous')], default='femme', max_length=10)),
                ('age_minimum', models.IntegerField(default=1)),
                ('age_maximum', models.IntegerField(default=100)),
            ],
        ),
        migrations.CreateModel(
            name='Wilaya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=2)),
                ('nom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('total_doses', models.IntegerField()),
                ('fabricant', models.CharField(max_length=50)),
                ('doses_administrées', models.IntegerField()),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utulisateurs.typevaccination')),
            ],
        ),
        migrations.CreateModel(
            name='Vaccination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dose_number', models.IntegerField(default=0)),
                ('dose_administre', models.IntegerField(default=1)),
                ('date_darnier_dose', models.DateField()),
                ('status', models.CharField(choices=[('en_attent', 'En_Attent'), ('certifie', 'Certifie'), ('abondanne', 'Abondanne')], default='en_attent', max_length=20)),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='vaccination_qr_codes/')),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utulisateurs.centredevaccination')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utulisateurs.patient')),
                ('vaccine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utulisateurs.vaccine')),
            ],
        ),
        migrations.CreateModel(
            name='Vaccin_Dose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utulisateurs.patient')),
                ('vaccin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utulisateurs.vaccine')),
                ('vaccination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utulisateurs.vaccination')),
            ],
        ),
        migrations.CreateModel(
            name='StockVaccins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeOperation', models.CharField(choices=[('AJOUTER', 'Addition'), ('SUPRIMER', 'Suppresion')], max_length=15)),
                ('quantite', models.PositiveIntegerField()),
                ('dateExpiration', models.DateField()),
                ('dateOperation', models.DateTimeField(auto_now_add=True)),
                ('numeroLot', models.CharField(default='I18207', max_length=50)),
                ('centerVaccination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utulisateurs.centredevaccination')),
                ('vaccine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utulisateurs.vaccine')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProchaineDose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_vaccination', models.DateField()),
                ('nombre_doses', models.IntegerField(default=2)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utulisateurs.patient')),
                ('vaccin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utulisateurs.vaccine')),
            ],
        ),
        migrations.CreateModel(
            name='Moughataa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('wilaya', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utulisateurs.wilaya')),
            ],
        ),
        migrations.CreateModel(
            name='HistoriqueStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeOperation', models.CharField(max_length=15)),
                ('quantite', models.PositiveIntegerField()),
                ('dateExpiration', models.DateField()),
                ('dateOperation', models.DateTimeField(auto_now_add=True)),
                ('numeroLot', models.CharField(default='I18207', max_length=50)),
                ('centerVaccination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utulisateurs.centredevaccination')),
                ('vaccine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utulisateurs.vaccine')),
            ],
        ),
        migrations.CreateModel(
            name='Dose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1)),
                ('duree', models.IntegerField()),
                ('vaccine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doses', to='utulisateurs.vaccine')),
            ],
        ),
        migrations.CreateModel(
            name='CertificatVaccination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_certificat', models.CharField(max_length=10, unique=True)),
                ('date_delivration', models.DateField()),
                ('valide', models.BooleanField(default=False)),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='vaccination_qr_codes/')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utulisateurs.patient')),
                ('vaccin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utulisateurs.vaccine')),
            ],
        ),
        migrations.AddField(
            model_name='centredevaccination',
            name='moughataa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utulisateurs.moughataa'),
        ),
        migrations.CreateModel(
            name='AdminCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('admin', 'Admin'), ('professionnel', 'Professionnel'), ('gerent-stock', 'Gerent-Stock')], default='admin', max_length=15)),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utulisateurs.centredevaccination')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]