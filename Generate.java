import java.io.*;

public class Generate {
	public static void main(String args[]) throws Exception {
		String prefix = "https://<some_url_here>/video240p_";
		FileWriter writer = new FileWriter("urls.txt");
		for(int i=0; i<2000; i++) {
			String videoId = "00000"+i;
			videoId = videoId.substring(videoId.length()-5, videoId.length());
			writer.write(prefix+videoId+".ts\n");
		}
		writer.close();
	}
}
