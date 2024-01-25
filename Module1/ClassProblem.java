import javax.swing.JOptionPane;

public class ClassProblem {

    public static void main(String[] args) {

        int startingNumber = 87;
        String results;
        String inputRequest;

        // Asks user for input of guess
        results = JOptionPane.showInputDialog(null, "Guess the lucky number ");

        // Convert the input to an integer
        int userGuess = Integer.parseInt(results);

        // Logic for input value
        if (userGuess == startingNumber) {
            inputRequest = "Great Guess";
        } else {
            inputRequest = "Sorry, try again...";
        }

        // Output end result
        JOptionPane.showMessageDialog(null, inputRequest);

    }
}