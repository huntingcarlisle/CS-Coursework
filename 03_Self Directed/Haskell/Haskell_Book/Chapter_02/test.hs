sayHello :: String -> IO ()
sayHello x =
    putStrLn ("Hello, " ++ x ++ "!")

triple x = x * 3

area_of_circle r = pi * (r * r)