# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import copy_metadata
import sys
from os import path
import platform
plat = platform.system().lower()

datas = []
datas += copy_metadata('tqdm')
datas += copy_metadata('regex')
datas += copy_metadata('requests')
datas += copy_metadata('packaging')
datas += copy_metadata('filelock')
datas += copy_metadata('numpy')
datas += copy_metadata('tokenizers')
datas += [(path.join(
    './.venv/Lib/site-packages' if plat == 'windows' else './.venv/lib/python3.9/site-packages',
    'moviepy'
), 'moviepy')]
datas += [(path.join(
    './.venv/Lib/site-packages' if plat == 'windows' else './.venv/lib/python3.9/site-packages',
    'imageio_ffmpeg'
), 'imageio_ffmpeg')]
datas += [(path.join(
    './.venv/Lib/site-packages' if plat == 'windows' else './.venv/lib/python3.9/site-packages',
    'torchaudio'
), 'torchaudio')]
datas += [(path.join(
    './.venv/Lib/site-packages' if plat == 'windows' else './.venv/lib/python3.9/site-packages',
    'whisper'
), 'whisper')]
datas += [(path.join(
    './.venv/Lib/site-packages' if plat == 'windows' else './.venv/lib/python3.9/site-packages',
    'opencc'
), 'opencc')]
datas += [('./snakers4_silero-vad_master', './snakers4_silero-vad_master')]

block_cipher = None


a = Analysis(
    ['autocut.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='autocut',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='autocut',
)
