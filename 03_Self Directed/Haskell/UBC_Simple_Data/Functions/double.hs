module Double where

check_expect' :: (Eq a) => a -> a -> Bool
check_expect' x y = x == y

main = do   print $check_expect' (double' 8) 16
            print $check_expect' (double' 4.2) (2 * 4.2)


double' :: (Num a) => a -> a
-- produce 2 times the given number

--double' n = 0     STUB

-- double' n = ... n     TEMPLATE

double' n = 2 * n