# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['Readingfromasqlfile.py', 'ReadingFromSqlModule.py'],
             pathex=['C:\\Users\\narut\\OneDrive\\Documents\\GitHub\\-finding-out-if-the-user-s-input-exists-by-reading-from-a-sql-database'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Readingfromasqlfile',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
