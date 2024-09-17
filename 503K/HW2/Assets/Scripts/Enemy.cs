using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Enemy : MonoBehaviour
{
    [SerializeField] private Transform target;
    [SerializeField] private float aggroRange = 10f;
    [SerializeField] private float speed = 3f;
    private Collision Collision;


    void Start() { 
    
        if(target == null)
        {
            GameObject playerPos = GameObject.Find("Player");
            if(playerPos != null )
            {
                target = playerPos.transform;
            }
            else
            {
                Debug.LogError("No GameObject named Player found in the scene");
            }
        }
    
    }
    // Update is called once per frame
    void Update()
    {
        float distanceToPlayer = Vector3.Distance(transform.position, target.position);

        if (distanceToPlayer < aggroRange) {
            MoveTowardsPlayer();
              }
    }

    private void OnCollisionEnter(Collision collision)
    {
        if(collision.gameObject.CompareTag("Bullet"))
        {
            Destroy(gameObject, 4f);
        }

    }
    private void MoveTowardsPlayer()
    {
        Vector3 direction = (target.position - transform.position).normalized;
        transform.position += direction * speed * Time.deltaTime;
        if (target != null)
        {
            transform.LookAt(target);
        }
    }
}
