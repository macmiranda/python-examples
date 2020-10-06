### Example 1 - Write a program, topN, that given an arbitrarily large file and a number, N, containing individual numbers on each line (e.g. 200Gb file), will output the largest N numbers, highest first. Tell me about the run time/space complexity of it, and whether you think there's room for improvement in your approach.

In pseudo code, using a linked list for the results, it would be something like:

    define N = max list size
    
    function orderedInsert (ordered list, current value){
           if ordered list size  = 0 or current value >= head node value
                 add node at the first position with current value
           else if current value > tail node value {
                 current node = get head node's next node
                 while ( true ){
                     if current value >= current node value
                          insert node with current value before current node and break the loop
                     if current node != tail node
                          current node = get next node
                     else
                          break the loop
                 }
            }
            else if ( size of list < N )
                  append node to the list with current value

            if ( size of list > N )
                remove last node of list
    }

    main(){
    ordered list = new ordered list

    while (current value != EOF ){
         current value = read line from file
         orderedInsert (ordered list, current value)
         current line = get next line
    }

    print ordered list
    }
----------------
Observations:
- the ordered list class must have an internal counter of the total number of nodes as a mean of not increasing the time complexity. It should also have pointers to the list's head and tail nodes.
- the sorted list is not comprised of unique values because that was not a requirement of the exercise.
----------------
Time complexity is greater than O(S x log N) but no more than O(S x N), where S is the number of lines in the file. Using a b-tree instead of an ordered linked list would make inserts faster - O(log N) -  but would add extra complexity to print the resulting list plus it requires more time to write the code. Opting for one or the other would depend on the urgency of the project, the available computational resources and ultimately the size of the file and the list.
 
Space complexity is always O(N).

------------------
How to use the program:

    Usage: ./topN.py <filename> <number N>
