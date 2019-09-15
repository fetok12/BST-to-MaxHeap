package mamudidiaarra;

public class Tekerlekli extends Gezgin implements EngelGecmeSuresiBul {

	public Tekerlekli(int sirasi, int yuku, String tipi, int motor_sayisi, int hizi) {
		super(sirasi, yuku, tipi, motor_sayisi, hizi);
		// TODO Auto-generated constructor stub
	}

	@Override
	public double EngelGecmeSuresiBul(int motor_sayisi) {
		return motor_sayisi*0.5;
		
	}

	



}
