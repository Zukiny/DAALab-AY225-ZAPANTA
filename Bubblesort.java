import java.awt.*;
import javax.swing.*;

public class BubbleSortGUI extends JFrame {
    private JTextArea inputArea;
    private JTextArea outputArea;
    private JButton sortButton;
    private JButton clearButton;
    private JComboBox<String> orderCombo;

    public BubbleSortGUI() {
        setTitle("Bubble Sort Visualizer");
        setSize(650, 520);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        initComponents();
    }

    private void initComponents() {
        setLayout(new BorderLayout(10, 10));

        // Title panel
        JPanel titlePanel = new JPanel();
        JLabel titleLabel = new JLabel("Bubble Sort Algorithm");
        titleLabel.setFont(new Font("Arial", Font.BOLD, 20));
        titlePanel.add(titleLabel);
        add(titlePanel, BorderLayout.NORTH);

        // Center panel with input and output
        JPanel centerPanel = new JPanel(new GridLayout(2, 1, 10, 10));

        // Input panel
        JPanel inputPanel = new JPanel(new BorderLayout(5, 5));
        inputPanel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        JLabel inputLabel = new JLabel("Enter numbers (comma-separated):");
        inputArea = new JTextArea(3, 40);
        inputArea.setText("64, 34, 25, 12, 22, 11, 90");
        inputArea.setFont(new Font("Monospaced", Font.PLAIN, 14));
        inputArea.setLineWrap(true);
        JScrollPane inputScroll = new JScrollPane(inputArea);

        // Order selector (new)
        JPanel orderPanel = new JPanel(new FlowLayout(FlowLayout.LEFT));
        JLabel orderLabel = new JLabel("Order:");
        orderCombo = new JComboBox<>(new String[] {"Ascending", "Descending"});
        orderCombo.setPreferredSize(new Dimension(140, 24));
        orderPanel.add(orderLabel);
        orderPanel.add(orderCombo);

        inputPanel.add(inputLabel, BorderLayout.NORTH);
        inputPanel.add(inputScroll, BorderLayout.CENTER);
        inputPanel.add(orderPanel, BorderLayout.SOUTH);

        // Output panel
        JPanel outputPanel = new JPanel(new BorderLayout(5, 5));
        outputPanel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        JLabel outputLabel = new JLabel("Results:");
        outputArea = new JTextArea(10, 40);
        outputArea.setEditable(false);
        outputArea.setFont(new Font("Monospaced", Font.PLAIN, 12));
        outputArea.setBackground(new Color(240, 240, 240));
        JScrollPane outputScroll = new JScrollPane(outputArea);
        outputPanel.add(outputLabel, BorderLayout.NORTH);
        outputPanel.add(outputScroll, BorderLayout.CENTER);

        centerPanel.add(inputPanel);
        centerPanel.add(outputPanel);
        add(centerPanel, BorderLayout.CENTER);

        // Button panel
        JPanel buttonPanel = new JPanel(new FlowLayout());
        sortButton = new JButton("Sort");
        clearButton = new JButton("Clear");

        sortButton.setPreferredSize(new Dimension(100, 30));
        clearButton.setPreferredSize(new Dimension(100, 30));

        sortButton.addActionListener(e -> performSort());
        clearButton.addActionListener(e -> clearFields());

        buttonPanel.add(sortButton);
        buttonPanel.add(clearButton);
        add(buttonPanel, BorderLayout.SOUTH);
    }

    private void performSort() {
        try {
            String input = inputArea.getText().trim();
            if (input.isEmpty()) {
                outputArea.setText("Please enter some numbers!");
                return;
            }

            String[] tokens = input.split(",");
            int[] arr = new int[tokens.length];

            for (int i = 0; i < tokens.length; i++) {
                arr[i] = Integer.parseInt(tokens[i].trim());
            }

            int[] original = arr.clone();
            boolean ascending = orderCombo.getSelectedItem().toString().equalsIgnoreCase("Ascending");

            long startTime = System.nanoTime();
            bubbleSort(arr, ascending);
            long endTime = System.nanoTime();
            double timeTakenMs = (endTime - startTime) / 1_000_000.0;

            StringBuilder result = new StringBuilder();
            result.append("Original Array:\n");
            result.append(arrayToString(original)).append("\n\n");
            result.append("Sorted Array (").append(ascending ? "Ascending" : "Descending").append("):\n");
            result.append(arrayToString(arr)).append("\n\n");
            result.append("Array Size: ").append(arr.length).append(" elements\n");
            result.append("Time Taken: ").append(String.format("%.6f", timeTakenMs)).append(" ms\n");
            result.append("Algorithm: Bubble Sort\n");
            result.append("Status: Sorting completed successfully!");

            outputArea.setText(result.toString());

        } catch (NumberFormatException e) {
            outputArea.setText("Error: Please enter valid integers separated by commas!");
        }
    }

    private void bubbleSort(int[] arr, boolean ascending) {
        int n = arr.length;

        for (int i = 0; i < n; i++) {
            boolean swapped = false;

            for (int j = 0; j < n - i - 1; j++) {
                boolean needSwap = ascending ? (arr[j] > arr[j + 1]) : (arr[j] < arr[j + 1]);
                if (needSwap) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }

            if (!swapped) {
                break;
            }
        }
    }

    private String arrayToString(int[] arr) {
        StringBuilder sb = new StringBuilder("[");
        for (int i = 0; i < arr.length; i++) {
            sb.append(arr[i]);
            if (i < arr.length - 1) {
                sb.append(", ");
            }
        }
        sb.append("]");
        return sb.toString();
    }

    private void clearFields() {
        inputArea.setText("");
        outputArea.setText("");
        orderCombo.setSelectedIndex(0);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            BubbleSortGUI gui = new BubbleSortGUI();
            gui.setVisible(true);
        });
    }
}
