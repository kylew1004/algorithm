// https://school.programmers.co.kr/learn/courses/30/lessons/118667?language=java

import java.util.*;

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        Queue<Integer> q1 = new LinkedList<>();
        Queue<Integer> q2 = new LinkedList<>();
        
        long target = 0;
        long total = 0;
        int mincnt = 0;
        
        for(int i = 0; i < queue1.length; i++) {
            q1.add(queue1[i]);
            q2.add(queue2[i]);
            target += (queue1[i] + queue2[i]);
            total += queue1[i];
        }
        target /= 2;
        
        while (target != total) {
            if (mincnt >= queue1.length * 3)
                return -1;
            
            if (total > target) {
                int tmp1 = q1.poll();
                total -= tmp1;
                q2.add(tmp1);
            }
            else {
                int tmp2 = q2.poll();
                total += tmp2;
                q1.add(tmp2);
            }
            mincnt++;
        }
        
        return mincnt;
    }
}