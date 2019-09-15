package mamudidiaarra;

public class Hibrit extends Robotlar implements EngelGecmeSuresiBul {
	int tasima_hizi;
	int tasima_kapasitesi;
	int kol_uzunluk;
	int hizi;
	String tipi2;
	
	
	public Hibrit(int sirasi, int yuku, String tipi, int motor_sayisi,int tasima_hizi, int tasima_kapasitesi, int kol_uzunluk, int hizi,String tipi2) {
		super(sirasi, yuku, tipi, motor_sayisi);
		this.tasima_hizi =tasima_hizi;
		this.tasima_kapasitesi=tasima_kapasitesi;
		this.kol_uzunluk=kol_uzunluk;
		this.hizi = hizi;
		this.tipi2=tipi2;
		
	}


	@Override
	public double EngelGecmeSuresiBul(int motor_sayisi) {
		if(this.tipi.equals("tekerlekli")) 
			return motor_sayisi*0.5;
		
		if(this.tipi.equals("paletli")) 
			return motor_sayisi*3;
		
		return 0;
	}

}
