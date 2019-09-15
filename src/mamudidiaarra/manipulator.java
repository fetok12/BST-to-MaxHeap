package mamudidiaarra;

public class manipulator extends Robotlar{
	int tasima_hizi;
	int tasima_kapasitesi;
	int kol_uzunluk;
	public manipulator(int sirasi, int yuku, String tipi, int motor_sayisi, int tasima_hizi,int tasima_kapasitesi, int kol_uzunluk) {
		super(sirasi, yuku, tipi, motor_sayisi);
		this.tasima_hizi =tasima_hizi;
		this.tasima_kapasitesi=tasima_kapasitesi;
		this.kol_uzunluk=kol_uzunluk;
	}

}
