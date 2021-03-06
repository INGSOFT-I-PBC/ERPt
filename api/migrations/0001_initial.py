# Generated by Django 4.0.6 on 2022-07-25 00:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("created_at", models.DateTimeField(auto_created=True, auto_now=True)),
                (
                    "id",
                    models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False),
                ),
                ("last_login", models.DateTimeField(blank=True, null=True, verbose_name="last login")),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("deleted_at", models.DateTimeField(default=None, null=True)),
                ("username", models.CharField(max_length=15, unique=True)),
                ("email", models.EmailField(max_length=100, unique=True, verbose_name="email address")),
                ("password", models.CharField(max_length=255)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "db_table": "user",
            },
        ),
        migrations.CreateModel(
            name="Group",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                ("codename", models.CharField(max_length=128)),
            ],
            options={
                "db_table": "group",
            },
        ),
        migrations.CreateModel(
            name="Permission",
            fields=[
                (
                    "id",
                    models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=50)),
                ("codename", models.CharField(max_length=128)),
            ],
            options={
                "db_table": "permission",
            },
        ),
        migrations.CreateModel(
            name="Role",
            fields=[
                (
                    "id",
                    models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=64, verbose_name="role name")),
                ("codename", models.CharField(default=None, max_length=50, verbose_name="role identifier")),
                (
                    "role_class",
                    models.CharField(
                        default=None, max_length=128, verbose_name="role class", db_column="class"
                    ),
                ),
            ],
            options={
                "db_table": "roles",
            },
        ),
        migrations.CreateModel(
            name="UserPermission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "permission",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.permission"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                "db_table": "user_permissions",
            },
        ),
        migrations.CreateModel(
            name="GroupPermission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("group", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.group")),
                (
                    "permission",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.permission"),
                ),
            ],
            options={
                "db_table": "group_permission",
            },
        ),
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=128)),
                ("lastname", models.CharField(max_length=128)),
                ("cid", models.CharField(max_length=11, unique=True)),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=True)),
                ("role", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.role")),
            ],
            options={
                "db_table": "employees",
            },
        ),
        migrations.AddField(
            model_name="user",
            name="employee",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="employee_info", to="api.employee"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="group",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT, related_name="permission_group", to="api.group"
            ),
        ),
    ]
