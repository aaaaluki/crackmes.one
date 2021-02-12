# Decompiled code
## main()
This is the main function

```c
undefined8 main(int argc,undefined8 *argv)

{
  size_t password_length;
  
  if (argc == 2) {
    password_length = strlen((char *)argv[1]);
    if (password_length == 10) {
      if (*(char *)(argv[1] + 4) == '@') {
        puts("Nice Job!!");
        printf("flag{%s}\n",argv[1]);
      }
      else {
        usage(*argv);
      }
    }
    else {
      usage(*argv);
    }
  }
  else {
    usage(*argv);
  }
  return 0;
}
```

## aux
This is an auxiliary function, it's used to show the usage of the compiled code.

```c
void usage(undefined8 argv0)

{
  printf("USAGE: %s <password>\n",argv0);
  puts("try again!");
                    /* WARNING: Subroutine does not return */
  exit(0);
}

```

## Solution
The first if checks if the number of arguments given is 2:
	- The executable itself.
	- The password.

`./rev50_linux64-bit <password>`

The second if checks the length of the password
	- The length of the password is 10.

The third if checks if the password + 4 is equal to @:
	- `(*(char *)(argv[1] + 4) == '@')`

Ascii values of @:
	- Dec := 64
	- Hex := 40
