# Buffer Overflow
Quick summary:
- Trigger a simple Stack Buffer Overflow bug with a bunch of `A`'s
- Discover the offset to a Saved Return Pointer with `pattern_create.rb`
- Confirm the discovered offset and gain tight `EIP` control
- Put stuff at a location that ESP points to at the time of the return to 
	the overwritten `Saved Return Pointer`
- Reason about and check for `bad characters`
- Find a `JMP ESP` gadget
- Generate shellcode with `msfvenom`
- Use `EIP control` and a `JMP ESP` gadget to cause execution of shellcode, 
	being mindful of the decoder stub's `GetPC` routine.

----

## Useful tools
- [Immunity Debugger](https://www.immunityinc.com/products/debugger/)
- [IDA](https://www.hex-rays.com/products/ida/)
- [radare2](https://github.com/radareorg/radare2)
- [gdb](https://www.gnu.org/software/gdb/)
    - [gef](https://github.com/hugsy/gef)
- [python3-pwntools](https://python3-pwntools.readthedocs.io/en/latest/)

----

## Useful links
- [DoStackBufferOverflowGood](https://github.com/justinsteven/dostackbufferoverflowgood)
