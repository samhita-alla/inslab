import java.io.*;
import java.lang.*;
class Encryption2
{
	public static void main (String args[])throws Exception
	{
		File r = new File("cipher.txt");
		FileReader fr=new FileReader("plain.txt");
		BufferedReader br=new BufferedReader(fr);

		FileWriter fw=new FileWriter(r);
		PrintWriter pw=new PrintWriter(fw);
		String s;
		System.out.println("<---Plain text--->");
		while((s=br.readLine())!=null)
		{
			System.out.println(s);
			for(int i=0;i<s.length();i++)
			{
				char c=s.charAt(i);
				if((c-97)>=0&&(c-97)<13)
					s=replaceCharAt(s, i, (char)(c+13));
				else
					s=replaceCharAt(s, i, (char)(c-13));
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
