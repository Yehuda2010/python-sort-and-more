import sorting as sort
import searching as search

def main():
    lst = [102, 34, 543, 101, 702, 89999, 844445]
    sort.quick_sort(lst)
    print(lst)
    print(search.binary_search(lst, 98))

if __name__ == "__main__":
    main()