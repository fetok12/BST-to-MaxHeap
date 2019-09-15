package mamudidiaarra;

import java.util.Scanner;
import java.awt.*;
import javax.swing.*;  
import java.util.*;


public class Main {

	public static void main(String[] args) {
		GRID application;
		Scanner scanner = new Scanner(System.in);
		String tipi;
		int i=1;
		int j=1;
		System.out.println("Robot sayisi giriniz:");
		int robot_sayisi = scanner.nextInt();
		scanner.nextLine();
		int min_hiz=0;
		int paletli_hiz=0;
		int tekerlekli_hiz=0;
		int yuk;
		int motor_sayisi;
		int hizi;
		int tasima_hizi;
		int seri_hiz=0;
		int paralel_hiz=0;
		int seri_tasima=0;
		int paralel_tasima=0;
		int tasima_kapasitesi;
		int kol_uzunluk;
		String haraketli;
		String haraketsiz;
		Spider spider_robot = null;
		Paletli paletli_robot = null;
		Tekerlekli tekerlekli_robot = null;
		Seri seri_robot = null;
		Paralel paralel_robot = null;
		Hibrit hibrit_robot= null;
		int ileri=0;
		int geri=0;
		int sag = 0;
		int sol=0;
		int sagdeger=0;
		int gerideger=0;
		double sure = 0;
		double ek_sure=0;
		double toplam_sure=0;
		double sure1 =0;
		int ilerideger=0;
		int soldeger=0;
		int sabitx = 0;
		int sabity = 0;
		int[][] matrix = new int[0][0];
		for(; i<=robot_sayisi; i++) {
			System.out.println(" Robot Sinifi giriniz:");
			String sinifi = scanner.nextLine();

			if(sinifi.equals("gezgin")) {
				System.out.println(" Robot tipini giriniz:");
				tipi = scanner.nextLine();
				System.out.println("Yukunu giriniz:");
				yuk = scanner.nextInt();
				scanner.nextLine();
				System.out.println("Motor sayisini giriniz:");
				motor_sayisi = scanner.nextInt();
				scanner.nextLine();
				System.out.println("Hizini giriniz (m/s):");
				hizi = scanner.nextInt();
				scanner.nextLine();	
				if(sinifi.toLowerCase().equals("gezgin") && tipi.toLowerCase().equals("spider")) {
					while(hizi>=paletli_hiz && paletli_hiz !=0 ) {
						System.out.println("Spider robot paletli robottan hizli olamaz. Hizi tekrar giriniz (m/s):");
						hizi = scanner.nextInt();
					}
					while( hizi>=tekerlekli_hiz && tekerlekli_hiz !=0 ) {
						System.out.println("Spider robot tekerlekli robottan hizli olamaz. Hizi tekrar giriniz (m/s):");
						hizi = scanner.nextInt();
					}
					 spider_robot = new Spider(i,yuk, tipi, motor_sayisi, hizi);
					 min_hiz= spider_robot.hizi;
					
				}
				
				if(sinifi.toLowerCase().equals("gezgin") && tipi.toLowerCase().equals("paletli")) {
					while(min_hiz>=hizi) {
						System.out.println("Spider robot paletli robottan hizli olamaz. Hizi tekrar giriniz (m/s):");
						 hizi = scanner.nextInt();
						
					}
					while(hizi>=tekerlekli_hiz && tekerlekli_hiz !=0) {
						System.out.println("paletli robot tekerlekli robottan hizli olamaz. Hizi tekrar giriniz (m/s):");
						hizi = scanner.nextInt();
					}
					
						paletli_robot = new Paletli(i,yuk, tipi, motor_sayisi, hizi);
						paletli_hiz=paletli_robot.hizi;
							
					
				}
				
				if(sinifi.toLowerCase().equals("gezgin") && tipi.equals("tekerlekli")) {
					while(min_hiz>=hizi || paletli_hiz>=hizi) {
						System.out.println("Tekerlekli robot spider yada paletliden daha hizli olmak zorundadir. Hizi tekrar giriniz (m/s):");
						hizi = scanner.nextInt();
					} 
						tekerlekli_robot = new Tekerlekli(i,yuk, tipi, motor_sayisi, hizi);
						tekerlekli_hiz = tekerlekli_robot.hizi;
					
					
				
				}
				
			}
			
			if(sinifi.equals("manipulator")) {
				System.out.println(" Robot tipini giriniz:");
				tipi = scanner.nextLine();
				System.out.println("Yukunu giriniz:");
				yuk = scanner.nextInt();
				scanner.nextLine();
				System.out.println("Tasima kapasitesini giriniz (m/s):");
				tasima_kapasitesi = scanner.nextInt();
				scanner.nextLine();
				while(yuk>tasima_kapasitesi) {
					System.out.println("Tasima kapasitesi yukunden kucuk olamaz. Tasima kapasitesini buyuk giriniz ");
					tasima_kapasitesi = scanner.nextInt();
				}
				System.out.println("Kol uzunlugunu giriniz giriniz m:");
				kol_uzunluk = scanner.nextInt();
				scanner.nextLine();
				System.out.println("Motor sayisini giriniz:");
				motor_sayisi = scanner.nextInt();
				scanner.nextLine();
				System.out.println("Tasima hizini giriniz (m/s):");
				tasima_hizi = scanner.nextInt();
				scanner.nextLine();
			
				if(tipi.toLowerCase().equals("seri")) {
					while(tasima_kapasitesi>=paralel_tasima && paralel_tasima !=0) {
						System.out.println("Seri robotun tasima kapasitesi Paralelden buyuk olamaz. lutfen tekrar deger girin");
						System.out.println(paralel_tasima);
						tasima_kapasitesi = scanner.nextInt();
					}
					while(tasima_hizi>=paralel_hiz && paralel_hiz !=0) {
						System.out.println("Seri robotun tasima hizi Paralelden buyuk olamaz. lutfen tekrar deger girin");
						tasima_hizi = scanner.nextInt();
					}
					seri_robot = new Seri(i, yuk, tipi, motor_sayisi, tasima_hizi, tasima_kapasitesi, kol_uzunluk);
					seri_tasima=seri_robot.tasima_kapasitesi;
					seri_hiz = seri_robot.tasima_hizi;
				}
				if(tipi.toLowerCase().equals("paralel")) {
					while(tasima_kapasitesi<=seri_tasima) {
						System.out.println("Paralel robotun tasima kapasitesi seri robottan kucuk olamaz. lutfen tekrar deger girin");
						tasima_kapasitesi = scanner.nextInt();
					}
					while(tasima_hizi<=seri_hiz) {
						System.out.println("Paralel robotun tasima hizi seri robottan kucuk olamaz. lutfen tekrar deger girin");
						tasima_hizi = scanner.nextInt();
					}
					paralel_robot = new Paralel(i, yuk, tipi, motor_sayisi, tasima_hizi, tasima_kapasitesi, kol_uzunluk);
					paralel_tasima=paralel_robot.tasima_kapasitesi;
					paralel_hiz = paralel_robot.tasima_hizi;
					
					
				}
				
			
				
			}
			if(sinifi.equals("hibrit")) {
				System.out.println(" hareketli kismi:");
				haraketli = scanner.nextLine();
				System.out.println(" hareketsiz kismi:");
				haraketsiz = scanner.nextLine();
				System.out.println("Yukunu giriniz:");
				yuk = scanner.nextInt();
				scanner.nextLine();
				System.out.println("Motor sayisini giriniz:");
				motor_sayisi = scanner.nextInt();
				scanner.nextLine();
				System.out.println("Hizini giriniz (m/s):");
				hizi = scanner.nextInt();
				scanner.nextLine();	
				System.out.println("Tasima kapasitesini giriniz:");
				tasima_kapasitesi = scanner.nextInt();
				scanner.nextLine();
				while(yuk>tasima_kapasitesi) {
					System.out.println("Tasima kapasitesi yukunden kucuk olamaz. Tasima kapasitesini buyuk giriniz ");
					tasima_kapasitesi = scanner.nextInt();
				}
				System.out.println("Kol uzunlugunu giriniz giriniz (m):");
				kol_uzunluk = scanner.nextInt();
				scanner.nextLine();
				System.out.println("Tasima hizini giriniz (m/s):");
				tasima_hizi = scanner.nextInt();
				scanner.nextLine();

					 hibrit_robot = new Hibrit(i,yuk, haraketli, motor_sayisi, tasima_hizi,tasima_kapasitesi,kol_uzunluk,hizi,haraketsiz);
				
				
			}
			
		
		
		}
		application = new GRID();
		for(; j<i; j++) {
			
			System.out.println("hangi siradaki robotu hakerek ettireceksiniz:");
			int sira = scanner.nextInt();
			if(tekerlekli_robot != null) {
				if(sira == tekerlekli_robot.sirasi){
					application.dispose();
					
					application = new GRID();
					application.kare(20, 810);
					
					//application.setDefaultCloseOperation( JFrame.EXIT_ON_CLOSE );
				System.out.println("Kac tane Engel gireceksiniz? (girmek istemiyorsaniz ise -1 e basin)");
				int engel_sayisi =0;
				engel_sayisi = scanner.nextInt();
				if(engel_sayisi !=-1) {
					 matrix = new int[engel_sayisi][2];
					System.out.println("(X,Y) Kordinaat duzleminde Engelleri giriniz");
					for(int a = 0; a < engel_sayisi; a++)
						for(int b = 0; b < 2; b++) {
							matrix[a][b] = scanner.nextInt();
						}	
					
				}
				
				
				if(engel_sayisi==1) {
					
					application.engel(matrix[0][0]*40-20,810-matrix[0][1]*40+40);
				}
				if(engel_sayisi==2) {
					application.engel(matrix[0][0]*40-20,810-matrix[0][1]*40+40);
					application.engel2(matrix[1][0]*40-20,810-matrix[1][1]*40+40);
				}
				if(engel_sayisi==3) {
					application.engel(matrix[0][0]*40-20,810-matrix[0][1]*40+40);
					application.engel2(matrix[1][0]*40-20,810-matrix[1][1]*40+40);
					application.engel3(matrix[2][0]*40-20,810-matrix[2][1]*40+40);
				}
				if(engel_sayisi==4) {
					application.engel(matrix[0][0]*40-20,810-matrix[0][1]*40+40);
					application.engel2(matrix[1][0]*40-20,810-matrix[1][1]*40+40);
					application.engel3(matrix[2][0]*40-20,810-matrix[2][1]*40+40);
					application.engel4(matrix[3][0]*40-20,810-matrix[3][1]*40+40);
				}
				if(engel_sayisi==5) {
					application.engel(matrix[0][0]*40-20,810-matrix[0][1]*40+40);
					application.engel2(matrix[1][0]*40-20,810-matrix[1][1]*40+40);
					application.engel3(matrix[2][0]*40-20,810-matrix[2][1]*40+40);
					application.engel4(matrix[3][0]*40-20,810-matrix[3][1]*40+40);
					application.engel5(matrix[4][0]*40-20,810-matrix[4][1]*40+40);
				}
				System.out.println("Hareket Komutlarini giriniz (gecen sureyi hesaplamak icin ise -1'i basin) ");
				while(sagdeger <21 && gerideger <21 && sagdeger>-1 && gerideger>-1) {
					     
					System.out.println("sag:");
					sag = scanner.nextInt();
					if(sag == -1 || sol == -1 || ileri == -1 || geri == -1) break;
					System.out.println("ileri:");
					ileri = scanner.nextInt();
					if(sag == -1 || sol == -1 || ileri == -1 || geri == -1) break;
					System.out.println("sol:");
					sol = scanner.nextInt();
					if(sag == -1 || sol == -1 || ileri == -1 || geri == -1) break;
					System.out.println("geri:");
					geri = scanner.nextInt();
					if(sag == -1 || sol == -1 || ileri == -1 || geri == -1) break;
					
					sagdeger = sag + sagdeger;
					 ilerideger=0;
					ilerideger = ileri + ilerideger;
					 soldeger=0;
					soldeger = sol + soldeger;
					gerideger = geri + gerideger;
					sagdeger= sagdeger-soldeger;
					gerideger= gerideger-ilerideger;
					
					 sure = ((sagdeger+gerideger)*10)/tekerlekli_robot.hizi;
					if(engel_sayisi !=-1) {
					 for(int a = 0; a < engel_sayisi; a++) {
						if((sagdeger == matrix[a][0] && gerideger >= matrix[a][1]) || (sagdeger >= matrix[a][0] && gerideger == matrix[a][1])) {
							System.out.println("Tekerlekli robot bir engelden gecti ");
							ek_sure=ek_sure + tekerlekli_robot.EngelGecmeSuresiBul(tekerlekli_robot.motor_sayisi);
						}
					}
					sure = sure + ek_sure;			
					}
				}
				if(sagdeger >20 || gerideger >20 || sagdeger <-1 || gerideger<-1) {
					System.out.println("Robotu izgaranin disina cikardiniz. Robot Sonlandirildi.");
				}else {
					application.kare(sagdeger*40-20,810-gerideger*40+40);
					application.sil(20,810);
					System.out.println("Gecen sure: "+sure);
				}
				//application.setVisible(false);
			}
			}

			if(paletli_robot != null) {
				if(sira == paletli_robot.sirasi){
					application.dispose();
					
					application = new GRID();
					application.kare(20, 810);
					
				System.out.println("Kac tane Engel gireceksiniz? (girmek istemiyorsaniz yada engel belirleme islemi bitti ise -1 e basin)");
				int engel_sayisi =0;
				engel_sayisi = scanner.nextInt();
				if(engel_sayisi !=-1) {
					 matrix = new int[engel_sayisi][2];
					System.out.println("(X,Y) Kordinaat duzleminde Engelleri giriniz");
					for(int a = 0; a < engel_sayisi; a++)
						for(int b = 0; b < 2; b++)
							matrix[a][b] = scanner.nextInt();
				}
				if(engel_sayisi==1) {
					
					application.engel(matrix[0][0]*40-20,810-matrix[0][1]*40+40);
				}
				if(engel_sayisi==2) {
					application.engel(matrix[0][0]*40-20,810-matrix[0][1]*40+40);
					application.engel2(matrix[1][0]*40-20,810-matrix[1][1]*40+40);
				}
				if(engel_sayisi==3) {
					application.engel(matrix[0][0]*40-20,810-matrix[0][1]*40+40);
					application.engel2(matrix[1][0]*40-20,810-matrix[1][1]*40+40);
					application.engel3(matrix[2][0]*40-20,810-matrix[2][1]*40+40);
				}
				if(engel_sayisi==4) {
					application.engel(matrix[0][0]*40-20,810-matrix[0][1]*40+40);
					application.engel2(matrix[1][0]*40-20,810-matrix[1][1]*40+40);
					application.engel3(matrix[2][0]*40-20,810-matrix[2][1]*40+40);
					application.engel4(matrix[3][0]*40-20,810-matrix[3][1]*40+40);
				}
				if(engel_sayisi==5) {
					application.engel(matrix[0][0]*40-20,810-matrix[0][1]*40+40);
					application.engel2(matrix[1][0]*40-20,810-matrix[1][1]*40+40);
					application.engel3(matrix[2][0]*40-20,810-matrix[2][1]*40+40);
					application.engel4(matrix[3][0]*40-20,810-matrix[3][1]*40+40);
					application.engel5(matrix[4][0]*40-20,810-matrix[4][1]*40+40);
				}
				System.out.println("Hareket Komutlarini giriniz (gecen sureyi hesaplamak icin ise -1'i basin) ");
				while(sagdeger <21 && gerideger <21 && sagdeger>-1 && gerideger>-1) {
					     
					System.out.println("sag:");
					sag = scanner.nextInt();
					if(sag == -1 || sol == -1 || ileri == -1 || geri == -1) break;
					System.out.println("ileri:");
					ileri = scanner.nextInt();
					if(sag == -1 || sol == -1 || ileri == -1 || geri == -1) break;
					System.out.println("sol:");
					sol = scanner.nextInt();
					if(sag == -1 || sol == -1 || ileri == -1 || geri == -1) break;
					System.out.println("geri:");
					geri = scanner.nextInt();
					if(sag == -1 || sol == -1 || ileri == -1 || geri == -1) break;
					
					sagdeger = sag + sagdeger;
					 ilerideger=0;
					ilerideger = ileri + ilerideger;
					 soldeger=0;
					soldeger = sol + soldeger;
					gerideger = geri + gerideger;
					sagdeger= sagdeger-soldeger;
					gerideger= gerideger-ilerideger;
					
					 sure = ((sagdeger+gerideger)*10)/paletli_robot.hizi;
					 if(engel_sayisi !=-1) {
						for(int a = 0; a < engel_sayisi; a++) {
						if((sagdeger == matrix[a][0] && gerideger >= matrix[a][1]) || (sagdeger >= matrix[a][0] && gerideger == matrix[a][1])) {
							System.out.println("Paletli robot bir engelden gecti ");
							ek_sure=ek_sure + paletli_robot.EngelGecmeSuresiBul(paletli_robot.motor_sayisi);
							}
						}
						sure = sure + ek_sure; 
					 }
	
					
				}
				if(sagdeger >20 || gerideger >20 || sagdeger <-1 || gerideger<-1) {
					System.out.println("Robotu izgaranin disina cikardiniz. Robot Sonlandirildi.");
				}else {
					application.kare(sagdeger*40-20,810-gerideger*40+40);
					application.sil(20,810);
					System.out.println("Gecen sure: "+sure);
				}
				
				
			}
			}

			if(spider_robot !=null) {
				 if(sira == spider_robot.sirasi){
					 application.dispose();
						
						application = new GRID();
						application.kare(20, 810);
				System.out.println("Kac tane Engel gireceksiniz? (girmek istemiyorsaniz yada engel belirleme islemi bitti ise -1 e basin)");
				int engel_sayisi =0;
				engel_sayisi = scanner.nextInt();
				if(engel_sayisi !=-1) {
					 matrix = new int[engel_sayisi][2];
					System.out.println("(X,Y) Kordinaat duzleminde Engelleri giriniz");
					for(int a = 0; a < engel_sayisi; a++)
						for(int b = 0; b < 2; b++)
							matrix[a][b] = scanner.nextInt();
				}
				
				if(engel_sayisi==1) {
					
					application.engel(matrix[0][0]*40-20,810-matrix[0][1]*40+40);
				}
				if(engel_sayisi==2) {
					application.engel(matrix[0][0]*40-20,810-matrix[0][1]*40+40);
					application.engel2(matrix[1][0]*40-20,810-matrix[1][1]*40+40);
				}
				if(engel_sayisi==3) {
					application.engel(matrix[0][0]*40-20,810-matrix[0][1]*40+40);
					application.engel2(matrix[1][0]*40-20,810-matrix[1][1]*40+40);
					application.engel3(matrix[2][0]*40-20,810-matrix[2][1]*40+40);
				}
				if(engel_sayisi==4) {
					application.engel(matrix[0][0]*40-20,810-matrix[0][1]*40+40);
					application.engel2(matrix[1][0]*40-20,810-matrix[1][1]*40+40);
					application.engel3(matrix[2][0]*40-20,810-matrix[2][1]*40+40);
					application.engel4(matrix[3][0]*40-20,810-matrix[3][1]*40+40);
				}
				if(engel_sayisi==5) {
					application.engel(matrix[0][0]*40-20,810-matrix[0][1]*40+40);
					application.engel2(matrix[1][0]*40-20,810-matrix[1][1]*40+40);
					application.engel3(matrix[2][0]*40-20,810-matrix[2][1]*40+40);
					application.engel4(matrix[3][0]*40-20,810-matrix[3][1]*40+40);
					application.engel5(matrix[4][0]*40-20,810-matrix[4][1]*40+40);
				}
				
				System.out.println("Hareket Komutlarini giriniz (gecen sureyi hesaplamak icin ise -1'e basin) ");
				while(sagdeger <21 && gerideger <21 && sagdeger>-1 && gerideger>-1) {
					     
					System.out.println("sag:");
					sag = scanner.nextInt();
					if(sag == -1 || sol == -1 || ileri == -1 || geri == -1) break;
					System.out.println("ileri:");
					ileri = scanner.nextInt();
					if(sag == -1 || sol == -1 || ileri == -1 || geri == -1) break;
					System.out.println("sol:");
					sol = scanner.nextInt();
					if(sag == -1 || sol == -1 || ileri == -1 || geri == -1) break;
					System.out.println("geri:");
					geri = scanner.nextInt();
					if(sag == -1 || sol == -1 || ileri == -1 || geri == -1) break;
					
					sagdeger = sag + sagdeger;
					 ilerideger=0;
					ilerideger = ileri + ilerideger;
					 soldeger=0;
					soldeger = sol + soldeger;
					gerideger = geri + gerideger;
					sagdeger= sagdeger-soldeger;
					gerideger= gerideger-ilerideger;
					
					 sure = ((sagdeger+gerideger)*10)/spider_robot.hizi;
					 if(engel_sayisi !=-1) {
						for(int a = 0; a < engel_sayisi; a++) {
						 if((sagdeger == matrix[a][0] && gerideger >= matrix[a][1]) || (sagdeger >= matrix[a][0] && gerideger == matrix[a][1])) {
							System.out.println("Spider robot engele carpti yon degistiriniz yada -1 e basip sureyi hesaplayin");
							break;
							}
						} 
					 }
					
					
				}
				if(sagdeger >20 || gerideger >20 || sagdeger <-1 || gerideger<-1) {
					System.out.println("Robotu izgaranin disina cikardiniz. Robot Sonlandirildi.");
				}else {
					application.kare(sagdeger*40-20,810-gerideger*40+40);
					application.sil(20,810);
					System.out.println("Gecen sure: "+sure);
				}
			}
			}
			if(paralel_robot != null) {
				if(sira == paralel_robot.sirasi){
					 application.dispose();
					application = new GRID();
				System.out.println("Baslangic konumunu giriniz (X,Y)");
				System.out.println("X Koordinati :");
				sagdeger = scanner.nextInt();
				System.out.println("Y Koordinati :");
				gerideger = scanner.nextInt();
				
				application.kare(sagdeger*40-20,810-gerideger*40+40);
				System.out.println("Hareket Komutlarini giriniz (gecen sureyi hesaplamak icin ise -1'i basin) ");
				while(1==1) {
					     
					System.out.println("sag:");
					sag = scanner.nextInt();
					if(sag  == -1 || sol  == -1 || ileri  == -1 || geri  == -1) break;
					System.out.println("ileri:");
					ileri = scanner.nextInt();
					if(sag  == -1 || sol  == -1 || ileri  == -1 || geri  == -1) break;
					System.out.println("sol:");
					sol  = scanner.nextInt();
					if(sag  == -1 || sol  == -1 || ileri  == -1 || geri  == -1) break;
					System.out.println("geri:");
					geri  = scanner.nextInt();
					if(sag  == -1 || sol  == -1 || ileri  == -1 || geri  == -1) break;
					
					sagdeger = sag + sagdeger;
				    ilerideger=0;
					ilerideger = ileri + ilerideger;
				    soldeger=0;
					soldeger = sol + soldeger;
					gerideger = geri + gerideger;
					sagdeger= sagdeger-soldeger;
					gerideger= gerideger-ilerideger;
					
					
					
					while((sag+geri)*10 > paralel_robot.kol_uzunluk) {
						System.out.println("Gidilen mesafe kol uzunlugunu asti lutfen uygun hareket bilgileri giriniz");
						System.out.println("sag:");
						sag = scanner.nextInt();
						if(sag  == -1 || sol  == -1 || ileri  == -1 || geri  == -1) break;
						System.out.println("ileri:");
						ileri = scanner.nextInt();
						if(sag  == -1 || sol  == -1 || ileri  == -1 || geri  == -1) break;
						System.out.println("sol:");
						sol = scanner.nextInt();
						if(sag  == -1 || sol  == -1 || ileri  == -1 || geri  == -1) break;
						System.out.println("geri:");
						geri = scanner.nextInt();
						if(sag  == -1 || sol  == -1 || ileri  == -1 || geri  == -1) break;
					}
					
					sure = ((sag+geri)*10)/paralel_robot.tasima_hizi;
					
				}
					application.yuk(sagdeger*40-20,810-gerideger*40+40);
				
					System.out.println("Gecen sure: "+sure);
				
			}
			}
			if(seri_robot != null) {
				if(sira == seri_robot.sirasi) {
					application.dispose();
					application = new GRID();
				System.out.println("Baslangic konumunu giriniz (X,Y)");
				System.out.println("X Koordinati :");
				sagdeger = scanner.nextInt();
				System.out.println("Y Koordinati :");
				gerideger = scanner.nextInt();
				application.kare(sagdeger*40-20,810-gerideger*40+40);
				System.out.println("Hareket Komutlarini giriniz (gecen sureyi hesaplamak icin ise -1'i basin) ");
				while(1==1) {
					     
					System.out.println("sag:");
					sag = scanner.nextInt();
					if(sag  == -1 || sol  == -1 || ileri  == -1 || geri  == -1) break;
					System.out.println("ileri:");
					ileri = scanner.nextInt();
					if(sag  == -1 || sol  == -1 || ileri  == -1 || geri  == -1) break;
					System.out.println("sol:");
					sol  = scanner.nextInt();
					if(sag  == -1 || sol  == -1 || ileri  == -1 || geri  == -1) break;
					System.out.println("geri:");
					geri  = scanner.nextInt();
					if(sag  == -1 || sol  == -1 || ileri  == -1 || geri  == -1) break;
					
					sagdeger = sag + sagdeger;
				    ilerideger=0;
					ilerideger = ileri + ilerideger;
				    soldeger=0;
					soldeger = sol + soldeger;
					gerideger = geri + gerideger;
					sagdeger= sagdeger-soldeger;
					gerideger= gerideger-ilerideger;
					
						while((sag+geri)*10 > seri_robot.kol_uzunluk) {
							System.out.println("Gidilen mesafe kol uzunlugunu asti lutfen uygun hareket bilgileri giriniz");
							System.out.println("sag:");
							sag = scanner.nextInt();
							if(sag  == -1 || sol  == -1 || ileri  == -1 || geri  == -1) break;
							System.out.println("ileri:");
							ileri = scanner.nextInt();
							if(sag  == -1 || sol  == -1 || ileri  == -1 || geri  == -1) break;
							System.out.println("sol:");
							sol = scanner.nextInt();
							if(sag  == -1 || sol  == -1 || ileri  == -1 || geri  == -1) break;
							System.out.println("geri:");
							geri = scanner.nextInt();
							if(sag  == -1 || sol  == -1 || ileri  == -1 || geri  == -1) break;
						}
						sure = ((sag+geri)*10)/seri_robot.tasima_hizi;
						
				}
					application.yuk(sagdeger*40-20,810-gerideger*40+40);
					System.out.println("Gecen sure: "+sure);
				
			}
			}
			if(hibrit_robot !=null) {
				if(sira == hibrit_robot.sirasi) {
					application.dispose();
					application = new GRID();
					application.kare(20, 810);
				System.out.println("sabitlenecegi konumunu giriniz (X,Y)");
				System.out.println("X Koordinati :");
				sabitx = scanner.nextInt();
				System.out.println("Y Koordinati :");
				sabity = scanner.nextInt();
				System.out.println("Kac tane Engel gireceksiniz? (girmek istemiyorsaniz yada engel belirleme islemi bitti ise -1 e basin)");
				int engel_sayisi =0;
				engel_sayisi = scanner.nextInt();
				if(engel_sayisi !=-1) {
					 matrix = new int[engel_sayisi][2];
					System.out.println("(X,Y) Kordinaat duzleminde Engelleri giriniz");
					for(int a = 0; a < engel_sayisi; a++)
						for(int b = 0; b < 2; b++)
							matrix[a][b] = scanner.nextInt();
				}
				if(engel_sayisi==1) {
					
					application.engel(matrix[0][0]*40-20,810-matrix[0][1]*40+40);
				}
				if(engel_sayisi==2) {
					application.engel(matrix[0][0]*40-20,810-matrix[0][1]*40+40);
					application.engel2(matrix[1][0]*40-20,810-matrix[1][1]*40+40);
				}
				if(engel_sayisi==3) {
					application.engel(matrix[0][0]*40-20,810-matrix[0][1]*40+40);
					application.engel2(matrix[1][0]*40-20,810-matrix[1][1]*40+40);
					application.engel3(matrix[2][0]*40-20,810-matrix[2][1]*40+40);
				}
				if(engel_sayisi==4) {
					application.engel(matrix[0][0]*40-20,810-matrix[0][1]*40+40);
					application.engel2(matrix[1][0]*40-20,810-matrix[1][1]*40+40);
					application.engel3(matrix[2][0]*40-20,810-matrix[2][1]*40+40);
					application.engel4(matrix[3][0]*40-20,810-matrix[3][1]*40+40);
				}
				if(engel_sayisi==5) {
					application.engel(matrix[0][0]*40-20,810-matrix[0][1]*40+40);
					application.engel2(matrix[1][0]*40-20,810-matrix[1][1]*40+40);
					application.engel3(matrix[2][0]*40-20,810-matrix[2][1]*40+40);
					application.engel4(matrix[3][0]*40-20,810-matrix[3][1]*40+40);
					application.engel5(matrix[4][0]*40-20,810-matrix[4][1]*40+40);
				}
				
				System.out.println("Sabitlenecegi konuma gitmek icin robota hareket konumlari giriniz ");
				
				while( !(sagdeger == sabitx && gerideger == sabity)) {
					
					System.out.println("sag:");
					sag = scanner.nextInt();
					System.out.println("ileri:");
					ileri = scanner.nextInt();
					System.out.println("sol:");
					sol = scanner.nextInt();
					System.out.println("geri:");
					geri = scanner.nextInt();
					
					sagdeger = sag + sagdeger;
					ilerideger=0;
					ilerideger = ileri + ilerideger;
					soldeger=0;
					soldeger = sol + soldeger;
					gerideger = geri + gerideger;
					sagdeger= sagdeger-soldeger;
					gerideger= gerideger-ilerideger;
					
					if(sagdeger >20 || gerideger >20 || sagdeger <-1 || gerideger<-1) {
						System.out.println("Robotu izgaranin disina cikardiniz. Robot Sonlandirildi.");
						break;
					}
					 sure = ((sagdeger+gerideger)*10)/hibrit_robot.hizi;
					 
					 if(engel_sayisi !=-1) {
						 for(int a = 0; a < engel_sayisi; a++) {
							if((sagdeger == matrix[a][0] && gerideger >= matrix[a][1]) || (sagdeger >= matrix[a][0] && gerideger == matrix[a][1])) {
								if(hibrit_robot.tipi.equals("spider")) {
									System.out.println("Hibrit Spider robot engele carpti");
									break;
								}
								System.out.println("Hibrit robot bir engelden gecti");
								ek_sure=ek_sure + hibrit_robot.EngelGecmeSuresiBul(hibrit_robot.motor_sayisi);
							
							}
						}
						sure = sure + ek_sure;
					 }
						
					
				}
				
				if(sagdeger <21 && gerideger <21 && sagdeger>-1 && gerideger>-1) {
					application.kare(sabitx*40-20,810-sabity*40+40);
					application.sil(20,810);
					System.out.println("Yuku kollarla tasimak icin konum bilgilerini giriniz: (gecen sureyi hesaplamak icin ise -1'i basin)");
					while(1==1) {
						     
						System.out.println("sag:");
						sag = scanner.nextInt();
						if(sag  == -1 || sol  == -1 || ileri  == -1 || geri  == -1) break;
						System.out.println("ileri:");
						ileri = scanner.nextInt();
						if(sag  == -1 || sol  == -1 || ileri  == -1 || geri  == -1) break;
						System.out.println("sol:");
						sol = scanner.nextInt();
						if(sag  == -1 || sol  == -1 || ileri  == -1 || geri  == -1) break;
						System.out.println("geri:");
						geri = scanner.nextInt();
						if(sag  == -1 || sol  == -1 || ileri  == -1 || geri  == -1) break;
						
						sagdeger = sag + sagdeger;
						ilerideger=0;
						ilerideger = ileri + ilerideger;
						soldeger=0;
						soldeger = sol + soldeger;
						gerideger = geri + gerideger;
						sagdeger= sagdeger-soldeger;
						gerideger= gerideger-ilerideger;
						
						 
							while((sag+geri)*10 > hibrit_robot.kol_uzunluk) {
								System.out.println("Gidilen mesafe kol uzunlugunu asti lutfen uygun hareket bilgileri giriniz");
								System.out.println("sag:");
								sag = scanner.nextInt();
								if(sag  == -1 || sol  == -1 || ileri  == -1 || geri  == -1) break;
								System.out.println("ileri:");
								ileri = scanner.nextInt();
								if(sag  == -1 || sol  == -1 || ileri  == -1 || geri  == -1) break;
								System.out.println("sol:");
								sol = scanner.nextInt();
								if(sag  == -1 || sol  == -1 || ileri  == -1 || geri  == -1) break;
								System.out.println("geri:");
								geri = scanner.nextInt();
								if(sag  == -1 || sol  == -1 || ileri  == -1 || geri  == -1) break;
								
							}
						sure1 = ((sag+geri)*10)/hibrit_robot.tasima_hizi;
						
					}
					toplam_sure=sure+sure1;
					application.yuk(sagdeger*40-20,810-gerideger*40+40);
					System.out.println("Gecen sure: "+toplam_sure);
				}
		
				}
			}

			
			//resetle degiskenleri
			 geri=0;
			 sag = 0;
			 sol=0;
			 ileri=0;
			 sagdeger=0;
			 gerideger=0;
			 sure = 0;
			 ek_sure=0;
			 toplam_sure=0;
			 sure1 =0;
			 ilerideger=0;
			 soldeger=0;
			 sabitx = 0;
			 sabity = 0;
			 matrix = new int[0][0];
			
		}
		
		

	}

}
