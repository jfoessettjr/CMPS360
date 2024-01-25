import javax.swing.*;

public class Survey {

    public static void main(String[] args) {
        String[] questions = {
                "What year did Sidney Crosby score his 500th goal?\nA. 2020 B. 2021 C. 2022",
                "What year did Evgeni Malkin score his 1200th point?\nA. 2023 B. 2022 C. 2021",
                "Which current NHL goaltender is the Pittsburgh Penguins leader in Wins?\nA. Tristan Jarry B. Marc-Andre Fleury C. Matt Murray"
        };

        char[] answers = {'C', 'A', 'B'};
        char ans = ' ';
        int x, correct = 0;
        String entry;
        boolean isGood;
        boolean[] correctness = new boolean[questions.length];

        for (x = 0; x < questions.length; ++x) {
            isGood = false;
            int firstError = 0;
            while (!isGood) {
                isGood = true;
                entry = JOptionPane.showInputDialog(null, questions[x]);
                ans = entry.charAt(0);
                if (ans != 'A' && ans != 'B' && ans != 'C') {
                    isGood = false;
                    if (firstError == 0) {
                        questions[x] = questions[x] +
                                "\nYour answer must be A, B, or C.";
                        firstError = 1;
                    }
                }
            }
            if (ans == answers[x]) {
                ++correct;
                correctness[x] = true;
                JOptionPane.showMessageDialog(null, "Correct!");
            } else {
                correctness[x] = false;
                JOptionPane.showMessageDialog(null, "The correct answer is " + answers[x]);
            }
        }

        StringBuilder resultMessage = new StringBuilder("Results:\n");
        for (int i = 0; i < questions.length; i++) {
            resultMessage.append("Question ").append(i + 1).append(": ");
            if (correctness[i]) {
                resultMessage.append("Correct\n");
            } else {
                resultMessage.append("Incorrect\n");
            }
        }

        JOptionPane.showMessageDialog(null, resultMessage.toString()
                + "You received " + correct + " right and\n" + (questions.length - correct) + " wrong");
    }
}