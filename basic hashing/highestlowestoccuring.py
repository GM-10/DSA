def main():
    n=int(input("Enter the size of the array: "))
    
    arr=input("Enter the elements of the array separated by space: ").split()
    freq={}
    for i in arr:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    print("Frequency of elements in the array is:",freq)
    highest_freq_element = max(freq, key=freq.get)
    lowest_freq_element = min(freq, key=freq.get)
    print("Element with highest frequency is:", highest_freq_element, "with frequency:", freq[highest_freq_element])
    print("Element with lowest frequency is:", lowest_freq_element, "with frequency:", freq[lowest_freq_element])

if __name__ == "__main__":
    main()