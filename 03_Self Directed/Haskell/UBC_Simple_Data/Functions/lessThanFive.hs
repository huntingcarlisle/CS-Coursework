module LessThanFive where

    check_expect' :: (Eq a) => a -> a -> Bool
    check_expect' x y = x == y
    
    main = do   print $check_expect' (less_than_five' "I am big!") False
                print $check_expect' (less_than_five' "") True
                print $check_expect' (less_than_five' "12345") False
                print $check_expect' (less_than_five' "1234") True
    
    
    less_than_five' :: String -> Bool
    -- check if string length is less than five
    
    -- less_than_five' str = False   -- stub
    less_than_five' str = length str < 5
