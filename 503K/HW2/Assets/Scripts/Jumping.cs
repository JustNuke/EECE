using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Jumping : MonoBehaviour
{
    Rigidbody rb;
    public float m_Thrust = 120f;
    bool isGrounded = true;
    bool isJumping = false;
    void Start()
    {
        rb = GetComponent<Rigidbody>();
    }

    // Update is called once per frame
    void Update()
    {
        if(isGrounded && !isJumping)
        {
            Debug.Log("isGrounded True");
        if (Input.GetButtonDown("Jump"))
            {
                Jump();
                isJumping = true;
            }
        }
    }

    private void Jump()
    {
        //rb.AddForce(transform.up * m_Thrust);
        rb.velocity = new Vector3(rb.velocity.x, m_Thrust, rb.velocity.z);
        isGrounded = false;
    }

    private void OnCollisionStay(Collision other)
    {
        Debug.Log("Colliding with ground");
        if(other.gameObject.layer == 6)
        {
            isGrounded = true;
            isJumping=false;
        }
    }

    private void OnCollisionExit(Collision other)
    {
    
        if (other.gameObject.layer == 6)
        {
            isGrounded = false;
            Debug.Log("Left ground");
        }
    }
}
