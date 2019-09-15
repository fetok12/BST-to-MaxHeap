package mamudidiaarra;
import java.awt.*;
import javax.swing.*;
public class GRID extends JFrame{

	int n;
	int m;
	int t;
	int k;
	int sd;
	int ds;
	int tr;
	int rt;
	int lk;
	int kl;
	int as;
	int sa;
	int counter;
	int silx;
	int sily;
	int yukx;
	int yuky;
	
	 public GRID()    {       
		 setSize( 850, 880 );
		 setVisible( true );
	
	
		 } 
	 public void kare(int a, int b) {
		 n=a;
		 m=b;
	 }
	 public void sil(int a, int b) {
		 silx=a;
		 sily=b;
	 }
	 public void yuk(int a, int b) {
		 yukx=a;
		 yuky=b;
	 }
	 public void engel(int a, int b) {
		 t=a;
		 k=b;
		
	 }
	 public void engel2(int a, int b) {
		 tr=a;
		 rt=b;
	
	 }
	 public void engel3(int a, int b) {
		 lk=a;
		 kl=b;

	 }
	 public void engel4(int a, int b) {
		 as=a;
		 sa=b;
	 }
	 public void engel5(int a, int b) {
		 sd=a;
		 ds=b;
	 }
	 public void paint( Graphics g )    
		 {  
		 for ( int x = 20; x <= 780; x += 40 )
		 for ( int y = 50; y <= 810; y += 40 ) 
		 g.drawRect( x, y,40,40 );
		 
		 g.fillRect (n,m, 40, 40); 
		 
		 g.setColor(Color.RED);
		 repaint();
			 g.fillRect (t,k, 40, 40); 
			 repaint();
			 g.fillRect (sd,ds, 40, 40); 
			 repaint();
			 g.fillRect (tr,rt, 40, 40); 
			 repaint();
			 g.fillRect (lk,kl, 40, 40); 
			 repaint();
			 g.fillRect (as,sa, 40, 40); 
			 repaint();
			 g.clearRect(silx, sily, 40,40);
			 repaint();
			 g.setColor(Color.BLUE);
			 repaint();
			 g.fillRect(yukx, yuky, 40,40);
			 repaint();

		 } 

}
