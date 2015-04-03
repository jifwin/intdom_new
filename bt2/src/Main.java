import com.intel.bluetooth.RemoteDeviceHelper;

import javax.bluetooth.RemoteDevice;
import java.io.IOException;
import java.util.Vector;

public class Main {

    public static void main(String[] args) throws IOException {
	RemoteDeviceDiscovery RDD = new RemoteDeviceDiscovery();
        Vector devices = RDD.getDevices();
        for (int i = 0; i < devices.size(); i++) {
            System.out.println(devices.elementAt(i).toString());
        }
        if (devices.elementAt(0).toString().equals("80CF417CE85D")) {
            RemoteDevice device = (RemoteDevice)devices.elementAt(0);
            System.out.print(device.getFriendlyName(true) + "\n");
            boolean paired = RemoteDeviceHelper.authenticate(device,"1111");
            System.out.println(paired);
            //tylko na 32 bitowej maszynie?
            //http://stackoverflow.com/questions/12896056/authentication-in-bluecove-linux-x64-not-working
            //http://homepages.ius.edu/RWISMAN/C490/html/JavaandBluetooth.htm
            //moze zmienic biblioteke
            //http://www.oracle.com/technetwork/articles/javame/index-140411.html
        }
    }
}
