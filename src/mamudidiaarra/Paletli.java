package mamudidiaarra;

public class Paletli extends Gezgin implements EngelGecmeSuresiBul {

	public Paletli(int sirasi, int yuku, String tipi, int motor_sayisi, int hizi) {
		super(sirasi, yuku, tipi, motor_sayisi, hizi);
		// TODO Auto-generated constructor stub
	}

	@Override
	public double EngelGecmeSuresiBul(int motor_sayisi) {
		// TODO Auto-generated method stub
		return motor_sayisi*3;
	}

	


	

}
