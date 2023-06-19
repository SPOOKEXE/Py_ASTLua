\-\-\-/CORE\
function\ GetChild\(Parent,\ Path,\ TimeOut\)\
\	local\ Current\ =\ Parent\
\
\	for\ _,\ V\ in\ string\.split\(Path,\ "/"\)\ do\
\	\	Current\ =\ Current:WaitForChild\(V,\ TimeOut\)\
\	end\
\
\	return\ Current\
end\
\
\-\-\[\[\
\	"multi\-line\-test"\
\]\]\
\
\-\-\-/SERVICES\
local\ ReplicatedStorage\ =\ game:GetService\("ReplicatedStorage"\)\
local\ UIS\ =\ game:GetService\("UserInputService"\)\
local\ P\ =\ game:GetService\("Players"\)\
local\ CLS\ =\ game:GetService\("CollectionService"\)\
\
\-\-\-/KNIT\
local\ Knit\ =\ require\(ReplicatedStorage\.Packages\.Knit\)\
\
local\ StandController\ =\ Knit\.CreateController\(\{\
\	Name\ =\ "StandController"\
\}\)\
\
\-\-\-/VARIABLES\
local\ Player\ =\ P\.LocalPlayer\
\
\-\-\-/FUNCTIONS\
\
function\ StandController:KnitInit\(\)\
\	\-\-\-/START\
\	print\(`Controller\ Initialized:\ \{StandController\.Name\}`\)\
\	\-\-\-/KNIT\|SERVER\
\	self\.StandService\ =\ Knit\.GetService\("StandService"\)\
end\
\
\-\-\[==\[\
\	fvsdfgdsfgadsgasdg\
\-\-\]==\]\
\
function\ StandController:KnitStart\(\)\
\	print\(`Controller\ Started:\ \{StandController\}`\)\
\	\-\-\-/CONNECTIONS\
\	self\.StandService\.onStandClaimed:Connect\(function\(Stand\ :\ Model\)\
\	\	local\ RootP\ :BasePart\ =\ Stand\.Root\
\	\	local\ Prompt\ :ProximityPrompt\ =\ RootP\.Claim\
\
\	\	local\ SurfaceGui\ =\ Stand:FindFirstChildWhichIsA\("GuiObject",\ true\)\
\	\	local\ Buttons\ =\ SurfaceGui\.MainFrame\.ScrollingFrame:GetChildren\(\)\
\
\	\	\-\-\-/CONFIGURATION\
\	\	Prompt\.ActionText\ =\ "UnClaim"\
\	\	Prompt\.ObjectText\ =\ "Hold\ E\ To\ UnClaim\ This\ Stand"\
\	\	Prompt\.Enabled\ =\ true\
\
\	\	\-\-\-/SEND\
\	\	Prompt\.Triggered:Once\(function\(\)\
\	\	\	\-\-\-/FIRE\
\	\	\	self\.StandService:UnclaimStand\(Stand\)\
\	\	\	\-\-/CONFIG\
\	\	\	Prompt\.ActionText\ =\ "Claim"\
\	\	\	Prompt\.ObjectText\ =\ "Hold\ E\ to\ claim\ this\ stand\."\
\	\	end\)\
\
\	\	for\ i,\ Button\ :\ GuiButton\ in\ Buttons\ do\
\
\	\	end\
\
\	end\)\
end\
\
return\ StandController