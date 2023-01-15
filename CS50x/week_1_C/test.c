public class Recursion {
        public static void main(String[] args) {
            System.out.println("Изначальный REC ( 15 , 9 )" );
            System.out.println(rec(15,9)); // запускаем sout с возвращаемым функцией [rec] результатом
        }

        static int rec (int m, int n) { // передаем в функцию [rec] 2 числа
            if(m % n == 0) { // если первое число [m] делится на второе число [n] нацело, то возвращаем его
                System.out.println("Окончателное число " + n);
                return n;
            } else {
                // если не делится нацело, то перезапускаем функцию и заносим в него другие аргументы :
                // в качестве первого уже будет второе число [n],
                // а в качестве второго будет остаток от деления первого[m] на второе[n] 15 / 9 = 1 (+ остаток 6)
                System.out.println("Заносим в REC (" + n + " , " + m % n + ")");
                return rec(n,m % n);
