import java.util.*;
import java.util.regex.*;
public class PasswordChecker
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter your password to check its strength");
        String password=sc.nextLine();
        int score=0;
        //if the password must atleast contain 9 characters
        //Every time a character is encountered the value of score is incremented

        if(password.length()>=9)
        {
            score++;
        }
        //It checks for the presence of an uppercase letter
        if(Pattern.compile("[A-Z]").matcher(password).find())
        {
            score++;
        }
        //It checks the presence of a lowercase letter and increments the score value
        if(Pattern.compile("[a-z]").matcher(password).find())
        {
            score++;
        }
        //It increments the score for every digit
        if(Pattern.compile("[0-9]").matcher(password).find())
        {
            score++;
        }
        if(Pattern.compile("[-_+=;!@#$%^&*(),.?\":{}|<>]").matcher(password).find())
        {
            score++;
        }
        //Based on the score value the strength of the password is decided
        if(score<=3)
        {
            System.out.println("Weak password");
        }
        else if(score==4)
        {
            System.out.println("Medium password");
        }
        else if(score>=5)
        {
            System.out.println("Strong password");
        }
        if(score>=15)
        {
            System.out.println("Your password is too long..Prone to threats..");
        }
        sc.close();
    }


}
