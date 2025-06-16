import java.awt.*;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

public class JavaXQTest extends Frame {

    public JavaXQTest() {
        setTitle("JavaXQ Test");
        setSize(400, 400);
        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) {
                System.exit(0);
            }
        });
    }

    public void paint(Graphics g) {
        JavaXQ javaXQ = new JavaXQ();
        javaXQ.drawRedE(50, 50, g);
        javaXQ.drawRedK(150, 50, g);
        javaXQ.drawRedA(250, 50, g);
        javaXQ.drawRedP(50, 150, g);
        javaXQ.drawBlkP(150, 150, g);
        javaXQ.drawBlkE(250, 150, g);
    }

    public static void main(String[] args) {
        JavaXQTest test = new JavaXQTest();
        test.setVisible(true);
    }
}
