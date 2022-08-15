from flask import render_template
from flask_login import login_required
from app.decorators import admin_required, permission_required
from app.models import Permission

from . import main


@main.get('/')
def index():
    return render_template('index.html')


@main.get('/protected')
@login_required
def protected_routes():
    return 'only authenticate users are allowed!'


@main.get('/admin')
@login_required
@admin_required
def for_admin_only():
    return "For administrators!"


@main.get('/pegawaitu')
@login_required
@permission_required(Permission.SURAT_KELUAR)
def for_admin_tu():
    return "for admin tu"


@main.get('/pegawai')
@login_required
@permission_required(Permission.SURAT_PERMOHONAN)
def for_pagawai():
    return "for staff"
