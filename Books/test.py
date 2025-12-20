# Online Python - IDE, Editor, Compiler, Interpreter

def sum(a, b, run):
    if run:
        print(run)
        return (a + b)
    else:
        return "bombers"

def main():
    a = int(input('Enter 1st number: '))
    b = int(input('Enter 2nd number: '))
    dry_run = {"true":True, "false":False}[input('Dry run True/False: ').lower()]
    if dry_run:
        print(f'Sum of {a} and {b} is {sum(a, b, dry_run)}')
    else:
        print(f"{sum(a, b, dry_run)}")
    
if __name__ == "__main__":
    main()