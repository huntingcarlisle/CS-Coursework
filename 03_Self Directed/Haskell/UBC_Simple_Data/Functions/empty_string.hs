module EmptyString where

    check_expect' :: (Eq a) => a -> a -> Bool
    check_expect' x y = x == y
    
    main = do   print $check_expect' (emptyString' "Test") False
                print $check_expect' (emptyString' "") True
                print $check_expect' (emptyString' "grass") False
                print $check_expect' (emptyString' "") True
    
    
    emptyString' :: String -> Bool
    -- Return True if string length is zero
    -- emptyString' str = False    --STUB
    emptyString' str = length str == 0

    
