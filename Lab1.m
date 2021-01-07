clear all; display('Part A');

%Request the user to enter a positive integer
    %x = input('Enter a positive number: ');
x = 10^9;
%Generate n random integers between -1000 to 1000 and save them in array a
a = randi([-1000 1000],1,x);
%Sort a
a = sort(a);
%{
%Linear_Search
disp(' ');
display('Linear Search');
tic
for i = 1:100
    %tic 
    %Pick a random number in a and save it in variable called key
    pos = randi(length(a));
    key = a(pos);

    %Call each function separately to search for the key in the given array
    LinearSearch(a,key);
    %toc(timerVal)
end 
toc

%Binary_Search
display('Binary Search');
tic
for i = 1:100
    %tic 
    %Pick a random number in a and save it in variable called key
    pos = randi(length(a));
    key = a(pos);

    %Call each function separately to search for the key in the given array
    BinarySearch(a,key);
    %toc(timerVal)
end 
toc
%}
%Part B
disp(' ');
display('Part B');
key1 = 5000;

disp(' ');
tic 
display('Linear Search');
%LinearSearch(a,key1);
toc 

tic
display('Binary Search');
BinarySearch(a,key1);
toc
disp(' ');


