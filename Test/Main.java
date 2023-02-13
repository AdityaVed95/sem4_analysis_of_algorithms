public class Main
{
  public static void main (String[]args)
  {
    int p = 0;
    int n = 1000;
    for (int i = 1; i < n; i = i * 2)
      {
        p++;
      }

    for (int j = 1; j < p; j = j * 2)
      {
	    System.out.println (j);
      }
  }
}
