# Example 1

## topN (and bottom too!)

This script reads a file containing one integer per line, and prints the N
largest and the N smallest integers.

## Usage

You can generate a bunch of integers with the following command:

```bash
python3 -c 'import random; f=open("numbers.txt","w"); [f.write(f"{random.randint(0,4294967295)}\n") for _ in range(250000000)]'
```

Then you can run the script:

```bash
python3 topN.py <filename> <N>
```
