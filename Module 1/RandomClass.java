import javax.swing.JOptionPane;
import java.util.Random;

public class RandomClass {
    public static void main(String[] args) {
        Random random = new Random();
        int randomNumber = random.nextInt(100); // Change 100 to the desired range
        JOptionPane.showMessageDialog(null, "Random Number: " + randomNumber);
    }
}
