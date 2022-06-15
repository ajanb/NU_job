%Get random coordinates in the bullet circle    
function Out = GetRandBullet(d,N)
    Out=rand(N,2);
    Out(:,1)=(d).*Out(:,1)-d/2;
    Out(:,2)=(2*sqrt(d*d*0.25-(Out(:,1)).^2)).*rand(N,1) - sqrt(d*d*0.25-(Out(:,1)).^2);
    Out=Out+[ones(N,1)*d/2, ones(N,1)*d/2];
    %scatter(Out(:,1),Out(:,2))
end