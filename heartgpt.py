# Importing sketchpy module
# To install sketchpy: pip install sketchpy

from sketchpy import library as lib

def main():
    print("Choose a sketch to draw:")
    print("1. Robert Downey Jr. (rdj)")
    print("2. APJ Abdul Kalam (apj)")
    print("3. BTS (bts)")
    print("4. vijay thala pati")
    print("5. Tom Holland (tom)")

    choice = int(input("Enter the number of your choice: "))

    if choice == 1:
        obj1 = lib.rdj()
        obj1.draw()
    elif choice == 2:
        obj2 = lib.apj()
        obj2.draw()
    elif choice == 3:
        obj3 = lib.bts()
        obj3.draw()
    elif choice == 4:
        obj4 = lib.vijay()
        obj4.draw()
    elif choice == 5:
        obj5 = lib.tom_holland()
        obj5.draw()
    else:
        print("Invalid choice!")
        return

    

if __name__ == "__main__":
    main()