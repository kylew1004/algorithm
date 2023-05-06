// https://school.programmers.co.kr/learn/courses/30/lessons/42577

import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        Arrays.sort(phone_book);
        Map<String, Integer> map = new HashMap<>();
        
        for (int i = 0; i<phone_book.length; i++)
        {
            map.put(phone_book[i], 1);
        }

        for (String s : phone_book)
        {
            for (int i = 1; i<s.length(); i++)
            {
                if (map.containsKey(s.substring(0, i)) == true)
                    return false;
            }
        }
        return true;
    }
}