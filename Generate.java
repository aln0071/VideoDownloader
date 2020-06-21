import java.io.*;

public class Generate {
	public static void main(String args[]) throws Exception {
	
		String prefix = "https://<some_url_here>/video240p_";	// The static part of the URL
		
		int videoIdLength = 5;					// The length of the dynamic part of URL ( Video Id ). Eg:- for a video id 00001, length is 5
		
		String paddingString = "0";				// The padding string used in the video id. Eg:- for a video id 00001, padding string is 0
		
		int startId = 0;					// The starting index of the video Ids
		
		int endId = 2000;					// The ending index of the video Ids
		
		FileWriter writer = new FileWriter("urls.txt");
		
		// This is the loop that creates the dynamic part of the URL. Modify the condition according to your needs
		for(int i=startId; i<=endId; i++) {
			String videoId = new String(new char[videoIdLength]).replace("\0", paddingString)+i;	// append id to the padding string
			videoId = videoId.substring(videoId.length()-videoIdLength, videoId.length());		// trim the video id to the fixed length
			writer.write(prefix+videoId+".ts\n");							// generate the URL and write it to urls.txt file
		}
		writer.close();
	}
}
