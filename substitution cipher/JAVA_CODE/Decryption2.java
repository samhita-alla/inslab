import java.io.*;
class Decryption2
{
	public static void main(String args[])throws Exception
	{
		FileReader fr=new FileReader("cipher.txt");
		BufferedReader br=new BufferedReader(fr);
		File w = new File("plain1.txt");
		FileWriter fw=new FileWriter(w);
		PrintWriter pw=new PrintWriter(fw);
		String s;
		System.out.println("<---Decrypted text--->");
		while((s=br.readLine())!=null)
		{
			for(int i=0;i<s.length();i++)
			{
				char c=s.charAt(i);
				int v=0;
				if((c-97)>=0&&(c-97)<13)
					s=replaceCharAt(s, i, (char)(c+13));
				else
					s=replaceCharAt(s, i, (char)(c-13));
				char y=(char)(v);
			}
			pw.write(s);
			System.out.println(s);
		}
		pw.close();
	}
	public static String replaceCharAt(String s, int pos, char c) {
    return s.substring(0, pos) + c + s.substring(pos + 1);
  }
}