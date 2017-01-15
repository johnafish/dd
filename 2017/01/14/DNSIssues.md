#DNS Issues
`github``dns`

When trying to set up the repo for this project, I ran into what seemed to be DNS issues. When trying to `ping github.com`, my terminal threw  the error: 

```
ping: cannot resolve github.com: Unknown host
```

After some searching, this issue was resolved by running:

```
sudo launchctl unload -w /System/Library/LaunchDaemons/com.apple.mDNSResponder.plist
sudo launchctl load -w /System/Library/LaunchDaemons/com.apple.mDNSResponder.plist
```

Not sure exactly what happened, but restarting my computer didn't help.

