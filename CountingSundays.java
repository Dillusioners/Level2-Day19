package DebJava;
import java.time.DayOfWeek;
import java.time.LocalDate;

public class CountingSundays {
    static int getSundays(LocalDate start_date, LocalDate end_date) {
        var sundays = 0;
        while (start_date.compareTo(end_date) <= 0) {
            if (start_date.getDayOfWeek().compareTo(DayOfWeek.SUNDAY) == 0) {
                sundays++;
            }
            start_date = start_date.plusMonths(1);
        }
        return sundays;
    }

    public static void main(String... args) {
        LocalDate start = LocalDate.of(1901, 1, 1);
        LocalDate end = LocalDate.of(2000, 12, 31);
        System.out.println("Total sundays that fell on 1st of the month = "+getSundays(start, end));
    }
}
