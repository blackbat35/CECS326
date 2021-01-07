function BinarySearch = BinarySearch(a, key)
	n = length(a);
    low = 0; 
    high = n - 1; 
    while low <= high
        mid = ceil((low + high)/2); 
        if a(mid) == key 
            break;
        else if a(mid) > key
            high = mid - 1;
            else 
            low = mid + 1;
            end 
        end 
    end 
end

